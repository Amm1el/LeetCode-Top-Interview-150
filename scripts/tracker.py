#!/usr/bin/env python3
"""LeetCode tracker for this repo. Standard library only.

Run from anywhere:
    python3 scripts/tracker.py new 27 "Remove Element" --difficulty Easy \
        --category "Array / String" --pattern "Two pointers (read/write)" --language java
    python3 scripts/tracker.py log 27 --confidence 4            # after a comprehension check
    python3 scripts/tracker.py log 27 --confidence 5 --review   # after a cold re-solve
    python3 scripts/tracker.py build                            # regenerate README dashboard
    python3 scripts/tracker.py week                             # this week's at-a-glance
    python3 scripts/tracker.py week --week 2026-W41
    python3 scripts/tracker.py due                              # what to re-solve today

Every problem lives in problems/NNNN-slug/ with a solution file and NOTES.md.
NOTES.md starts with a front-matter block that this script reads and writes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
WEEKLY = ROOT / "weekly"
README = ROOT / "README.md"

# Sections of the Top Interview 150 study plan, with problem counts.
CATEGORIES = [
    ("Array / String", 24), ("Two Pointers", 5), ("Sliding Window", 4), ("Matrix", 5),
    ("Hashmap", 9), ("Intervals", 4), ("Stack", 5), ("Linked List", 11),
    ("Binary Tree General", 14), ("Binary Tree BFS", 4), ("Binary Search Tree", 3),
    ("Graph General", 6), ("Graph BFS", 3), ("Trie", 3), ("Backtracking", 7),
    ("Divide & Conquer", 4), ("Kadane's Algorithm", 2), ("Binary Search", 7),
    ("Heap", 4), ("Bit Manipulation", 6), ("Math", 6), ("1D DP", 5),
    ("Multidimensional DP", 9),
]
PLAN_TOTAL = sum(n for _, n in CATEGORIES)

LANG_EXT = {"python": "py", "java": "java", "cpp": "cpp", "c++": "cpp", "javascript": "js",
            "typescript": "ts", "go": "go", "c": "c", "kotlin": "kt", "rust": "rs"}
LANG_NAME = {"py": "Python", "java": "Java", "cpp": "C++", "js": "JavaScript",
             "ts": "TypeScript", "go": "Go", "c": "C", "kt": "Kotlin", "rs": "Rust"}

# Days until the next cold re-solve, by confidence (1 = could not explain it, 5 = could teach it).
INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}
MAX_INTERVAL = 90

FIELDS = ["id", "title", "slug", "difficulty", "category", "pattern", "language", "status",
          "first_solved", "confidence", "reviews", "streak", "last_reviewed", "next_review"]
DONE = {"solved", "assisted"}

REVIEW_LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2}) · (check|re-solve) · confidence (\d)", re.M)

NOTES_TEMPLATE = """
## The problem in one sentence
_In your own words, no copying the prompt._

## Key insight
_The one idea that, if you remember only this, lets you rebuild the whole solution._

## Approach
_Steps in plain English. What does each pointer / variable / structure represent?_

## Complexity
- Time:
- Space:

## Edge cases
-

## What tripped me up
-

## Comprehension check
_Questions asked after solving, a summary of the answer, and a verdict._

## Review log
"""


# ---------------------------------------------------------------- notes I/O

def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def parse_notes(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise SystemExit(f"{path}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)


def write_notes(path: Path, meta: dict, body: str) -> None:
    lines = ["---"]
    for k in FIELDS:
        v = meta.get(k, "")
        v = "" if v is None else str(v)
        if any(c in v for c in ":#") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
            v = f'"{v}"'
        lines.append(f"{k}: {v}".rstrip())
    lines.append("---")
    path.write_text("\n".join(lines) + "\n\n" + body.lstrip("\n"), encoding="utf-8")


def date(s: str | None) -> dt.date | None:
    try:
        return dt.date.fromisoformat(s) if s else None
    except ValueError:
        return None


def to_int(s, default=0) -> int:
    try:
        return int(s)
    except (TypeError, ValueError):
        return default


def load_all() -> list[dict]:
    out = []
    if not PROBLEMS.exists():
        return out
    for d in sorted(PROBLEMS.iterdir()):
        notes = d / "NOTES.md"
        if not notes.is_file():
            continue
        meta, body = parse_notes(notes)
        meta["_dir"] = d
        meta["_body"] = body
        meta["_reviews"] = [(dt.date.fromisoformat(a), kind, int(c))
                            for a, kind, c in REVIEW_LINE.findall(body)]
        sol = [f for f in d.iterdir() if f.name.startswith("solution")]
        meta["_solution"] = sol[0] if sol else None
        out.append(meta)
    out.sort(key=lambda p: to_int(p.get("id")))
    return out


def find(problem_id: int) -> dict:
    for p in load_all():
        if to_int(p.get("id")) == problem_id:
            return p
    raise SystemExit(f"Problem {problem_id} not found under problems/. Run `new` first.")


# ---------------------------------------------------------------- formatting helpers

def bar(done: int, total: int, width: int = 20) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def conf_str(p: dict) -> str:
    c = to_int(p.get("confidence"))
    return f"{c}/5" if c else "—"


def lc_link(p: dict) -> str:
    return f"[{p['title']}](https://leetcode.com/problems/{p['slug']}/)"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def week_bounds(iso_week: str | None) -> tuple[dt.date, dt.date, str]:
    if iso_week:
        y, w = re.fullmatch(r"(\d{4})-W(\d{1,2})", iso_week).groups()
        start = dt.date.fromisocalendar(int(y), int(w), 1)
    else:
        today = dt.date.today()
        start = today - dt.timedelta(days=today.weekday())
    y, w, _ = start.isocalendar()
    return start, start + dt.timedelta(days=6), f"{y}-W{w:02d}"


# ---------------------------------------------------------------- commands

def cmd_new(a) -> None:
    slug = a.slug or slugify(a.title)
    d = PROBLEMS / f"{a.id:04d}-{slug}"
    d.mkdir(parents=True, exist_ok=True)
    notes = d / "NOTES.md"
    if notes.exists():
        raise SystemExit(f"{notes} already exists")
    ext = LANG_EXT.get(a.language.lower(), a.language.lower())
    sol = d / f"solution.{ext}"
    if not sol.exists():
        sol.write_text("", encoding="utf-8")
    meta = {"id": a.id, "title": a.title, "slug": slug, "difficulty": a.difficulty,
            "category": a.category, "pattern": a.pattern or "", "language": LANG_NAME.get(ext, ext),
            "status": a.status, "first_solved": a.date or dt.date.today().isoformat(),
            "confidence": "", "reviews": 0, "streak": 0, "last_reviewed": "", "next_review": ""}
    write_notes(notes, meta, NOTES_TEMPLATE)
    print(f"Created {rel(d)}/ (solution.{ext}, NOTES.md)")


def cmd_log(a) -> None:
    p = find(a.id)
    when = date(a.date) or dt.date.today()
    conf = a.confidence
    reviews = to_int(p.get("reviews")) + (1 if a.review else 0)
    streak = to_int(p.get("streak"))
    streak = streak + 1 if conf >= 4 else 0
    interval = INTERVALS[conf]
    if conf >= 4 and streak > 1:
        interval = min(MAX_INTERVAL, interval * 2 ** (streak - 1))
    p.update({"confidence": conf, "reviews": reviews, "streak": streak,
              "last_reviewed": when.isoformat(),
              "next_review": (when + dt.timedelta(days=interval)).isoformat()})
    if a.status:
        p["status"] = a.status
    kind = "re-solve" if a.review else "check"
    line = f"- {when.isoformat()} · {kind} · confidence {conf}"
    if a.note:
        line += f" · {a.note}"
    body = p["_body"].rstrip() + "\n" + line + "\n"
    write_notes(p["_dir"] / "NOTES.md", p, body)
    print(f"#{p['id']} {p['title']}: confidence {conf}, next re-solve {p['next_review']} (in {interval} days)")


def due_list(problems: list[dict], on: dt.date) -> list[dict]:
    due = [p for p in problems if p.get("status") in DONE
           and (date(p.get("next_review")) or dt.date.min) <= on]
    return sorted(due, key=lambda p: (date(p.get("next_review")) or dt.date.min, to_int(p.get("confidence"))))


def cmd_due(a) -> None:
    today = dt.date.today()
    due = due_list(load_all(), today)
    if not due:
        print("Nothing due. Go solve something new.")
        return
    for p in due:
        nr = p.get("next_review") or "never checked"
        print(f"#{p['id']:>4} {p['title']:<45} confidence {conf_str(p):<4} due {nr}")


def cmd_build(a) -> None:
    problems = load_all()
    today = dt.date.today()
    done = [p for p in problems if p.get("status") in DONE]
    in_plan = [p for p in done if p.get("category") in dict(CATEGORIES)]
    diff = Counter(p.get("difficulty", "?") for p in done)
    assisted = sum(1 for p in done if p.get("status") == "assisted")
    by_cat = Counter(p.get("category") for p in in_plan)

    # Activity streak: consecutive days up to today (or yesterday) with a solve or review.
    active = {date(p.get("first_solved")) for p in done} | {r[0] for p in problems for r in p["_reviews"]}
    active.discard(None)
    streak, day = 0, today if today in active else today - dt.timedelta(days=1)
    while day in active:
        streak += 1
        day -= dt.timedelta(days=1)

    out = ["# LeetCode Top Interview 150", "",
           "My solutions to the [LeetCode Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) "
           "study plan. Every problem has a solution plus notes on the key insight, complexity, edge cases, "
           "and a comprehension check, and gets re-solved from scratch on a spaced schedule.", "",
           f"_Dashboard generated {today.isoformat()} by `scripts/tracker.py build`._", "",
           "## Progress", "",
           f"**{len(in_plan)} / {PLAN_TOTAL}** `{bar(len(in_plan), PLAN_TOTAL, 30)}` "
           f"{100 * len(in_plan) / PLAN_TOTAL:.0f}%", "",
           "| Easy | Medium | Hard | Solved with help | Current streak |",
           "|---|---|---|---|---|",
           f"| {diff['Easy']} | {diff['Medium']} | {diff['Hard']} | {assisted} | {streak} day{'s' if streak != 1 else ''} |",
           ""]

    due = due_list(problems, today)
    out += ["## Due for a cold re-solve", ""]
    if due:
        out += ["| # | Problem | Confidence | Due |", "|---|---|---|---|"]
        out += [f"| {p['id']} | [{p['title']}]({rel(p['_dir'])}/NOTES.md) | {conf_str(p)} | "
                f"{p.get('next_review') or 'not yet checked'} |" for p in due]
    else:
        out.append("Nothing due.")
    out.append("")

    out += ["## By category", "", "| Category | Done | |", "|---|---|---|"]
    for name, total in CATEGORIES:
        n = by_cat.get(name, 0)
        out.append(f"| {name} | {n}/{total} | `{bar(n, total, 10)}` |")
    out.append("")

    pats = defaultdict(list)
    for p in done:
        pats[p.get("pattern") or "Unlabeled"].append(p)
    out += ["## By pattern", "", "Details and templates in [PATTERNS.md](PATTERNS.md).", ""]
    for name in sorted(pats, key=lambda k: (-len(pats[k]), k)):
        ids = ", ".join(f"[{p['id']}]({rel(p['_dir'])}/NOTES.md)" for p in pats[name])
        out.append(f"- **{name}** ({len(pats[name])}): {ids}")
    out.append("")

    out += ["## All problems", "",
            "| # | Problem | Difficulty | Category | Pattern | Lang | Status | Confidence | Code | Notes |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for p in problems:
        sol = f"[code]({rel(p['_solution'])})" if p["_solution"] else ""
        out.append(f"| {p['id']} | {lc_link(p)} | {p.get('difficulty', '')} | {p.get('category', '')} | "
                   f"{p.get('pattern', '')} | {p.get('language', '')} | {p.get('status', '')} | {conf_str(p)} | "
                   f"{sol} | [notes]({rel(p['_dir'])}/NOTES.md) |")
    out.append("")

    weeks = sorted(WEEKLY.glob("*.md"), reverse=True) if WEEKLY.exists() else []
    out += ["## Weekly at-a-glance", ""]
    out += [f"- [{w.stem}]({rel(w)})" for w in weeks[:8]] or ["None yet."]
    out += ["", "## How this repo works", "",
            "- `problems/NNNN-slug/` holds `solution.*` and `NOTES.md` (front matter + notes).",
            "- Confidence is 1–5 and sets the next cold re-solve: 1 → 1 day, 2 → 3, 3 → 7, 4 → 14, 5 → 30, "
            "doubling for each consecutive 4+ (max 90).",
            "- `solved with help` means a hint or the editorial was used. Those always get re-solved.",
            "- Workflow and the comprehension-check protocol are in [CLAUDE.md](CLAUDE.md).", ""]
    README.write_text("\n".join(out), encoding="utf-8")
    print(f"README.md rebuilt: {len(in_plan)}/{PLAN_TOTAL} done, {len(due)} due")


def cmd_week(a) -> None:
    start, end, label = week_bounds(a.week)
    problems = load_all()
    inweek = lambda d: d is not None and start <= d <= end  # noqa: E731

    new = [p for p in problems if p.get("status") in DONE | {"in-progress"} and inweek(date(p.get("first_solved")))]
    reviews = [(p, r) for p in problems for r in p["_reviews"] if inweek(r[0])]
    resolves = [(p, r) for p, r in reviews if r[1] == "re-solve"]
    checks = {p["id"]: r[2] for p, r in reviews if r[1] == "check"}
    active_days = {date(p.get("first_solved")) for p in new} | {r[0] for _, r in reviews}
    confs = [r[2] for _, r in reviews]
    avg = f"{sum(confs) / len(confs):.1f}" if confs else "—"
    assisted = [p for p in new if p.get("status") == "assisted"]

    nxt_start, nxt_end = end + dt.timedelta(days=1), end + dt.timedelta(days=7)
    upcoming = [p for p in problems if p.get("status") in DONE
                and (date(p.get("next_review")) or dt.date.min) <= nxt_end]
    shaky = sorted({p["id"]: p for p, r in reviews if r[2] <= 2}.values(), key=lambda p: to_int(p["id"]))
    done_total = sum(1 for p in problems if p.get("status") in DONE and p.get("category") in dict(CATEGORIES))

    path = WEEKLY / f"{label}.md"
    reflection = ("## Reflection\n\n"
                  "_Filled in during the weekly review._\n\n"
                  "- Hardest problem and why:\n"
                  "- Pattern I can now spot on sight:\n"
                  "- Pattern I still can't:\n"
                  "- Mistake I keep repeating:\n"
                  "- Focus for next week:\n")
    marker = "<!-- reflection: everything below is kept when this file is regenerated -->"
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if marker in old:
            reflection = old.split(marker, 1)[1].lstrip("\n")

    fmt = lambda d: d.strftime("%b %-d")  # noqa: E731
    out = [f"# Week {label[-2:]} · {fmt(start)} – {fmt(end)}, {end.year}", "",
           "## At a glance", "",
           "| New problems | Cold re-solves | Solved with help | Avg confidence | Active days | Plan progress |",
           "|---|---|---|---|---|---|",
           f"| {len(new)} | {len(resolves)} | {len(assisted)} | {avg} | {len(active_days)}/7 | "
           f"{done_total}/{PLAN_TOTAL} |", "",
           "## New this week", ""]
    if new:
        out += ["| Day | # | Problem | Difficulty | Pattern | Status | Check |", "|---|---|---|---|---|---|---|"]
        for p in sorted(new, key=lambda p: (p.get("first_solved"), to_int(p["id"]))):
            day = date(p["first_solved"]).strftime("%a")
            c = checks.get(p["id"])
            out.append(f"| {day} | {p['id']} | [{p['title']}](../{rel(p['_dir'])}/NOTES.md) | "
                       f"{p.get('difficulty', '')} | {p.get('pattern', '')} | {p.get('status', '')} | "
                       f"{f'{c}/5' if c else '—'} |")
    else:
        out.append("None.")
    out += ["", "## Cold re-solves", ""]
    if resolves:
        out += [f"- {r[0].strftime('%a')}: #{p['id']} {p['title']}, confidence {r[2]}/5" for p, r in resolves]
    else:
        out.append("None.")
    out += ["", "## Patterns touched", ""]
    pc = Counter((p.get("pattern") or "Unlabeled") for p in new) + Counter(
        (p.get("pattern") or "Unlabeled") for p, _ in resolves)
    out += [f"- {k}: {v}" for k, v in pc.most_common()] or ["None."]
    out += ["", "## Shaky (confidence 2 or below)", ""]
    out += [f"- #{p['id']} {p['title']}" for p in shaky] or ["None."]
    out += ["", f"## Due by {fmt(nxt_end)}", ""]
    out += [f"- #{p['id']} {p['title']} ({conf_str(p)}, due {p.get('next_review') or 'now'})"
            for p in sorted(upcoming, key=lambda p: p.get("next_review") or "")] or ["Nothing scheduled."]
    out += ["", marker, "", reflection.rstrip(), ""]
    WEEKLY.mkdir(exist_ok=True)
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {rel(path)}")


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new", help="scaffold a problem folder")
    n.add_argument("id", type=int)
    n.add_argument("title")
    n.add_argument("--slug")
    n.add_argument("--difficulty", required=True, choices=["Easy", "Medium", "Hard"])
    n.add_argument("--category", required=True, help='study-plan section, e.g. "Two Pointers", or "Other"')
    n.add_argument("--pattern", default="")
    n.add_argument("--language", default="python")
    n.add_argument("--status", default="solved", choices=["solved", "assisted", "in-progress"])
    n.add_argument("--date", help="YYYY-MM-DD, defaults to today")
    n.set_defaults(func=cmd_new)

    lg = sub.add_parser("log", help="record a comprehension check or a cold re-solve")
    lg.add_argument("id", type=int)
    lg.add_argument("--confidence", type=int, required=True, choices=range(1, 6))
    lg.add_argument("--review", action="store_true", help="this was a cold re-solve, not the first check")
    lg.add_argument("--status", choices=["solved", "assisted", "in-progress"])
    lg.add_argument("--note", default="")
    lg.add_argument("--date")
    lg.set_defaults(func=cmd_log)

    sub.add_parser("build", help="regenerate README.md").set_defaults(func=cmd_build)
    sub.add_parser("due", help="list problems due for a re-solve").set_defaults(func=cmd_due)
    wk = sub.add_parser("week", help="generate weekly/YYYY-Www.md")
    wk.add_argument("--week", help="ISO week like 2026-W41, defaults to the current week")
    wk.set_defaults(func=cmd_week)

    a = ap.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
