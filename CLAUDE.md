# How this repo is run

Ammiel does 1–3 LeetCode problems a day, working through Top Interview 150. Claude's job is not to praise solutions. It is to find out whether he actually understands each one well enough to rebuild it cold in an interview, record that honestly here, and schedule re-solves until it sticks.

Be direct. If an answer is vague, hand-wavy, or wrong, say so and ask again. Do not give the answer until he has made a real attempt.

## Python primer (before LeetCode)

He's doing `python-primer/` first: eight lessons over two days, hard stop Friday Oct 9, 2026. Don't let it stretch past that; push him to start problems.

When he finishes a lesson:
1. Read his exercise file (pulled from the repo or pasted). Run it. Passing tests aren't enough: flag non-idiomatic Python (index loops where `enumerate` fits, `range(len(...))`, string `+=` in loops, manual counting where `Counter` fits, Java habits) and any hidden complexity cost.
2. Ask 3–4 questions: one "predict the output" he hasn't seen, one "what does this cost and why", and one or two on the lesson's traps. Push back on vague answers.
3. If it's solid, tick the lesson's box in `python-primer/README.md`, commit `Primer: lesson NN`, push. If not, say exactly what to redo.

Exit test after lesson 08: 10 rapid-fire questions mixed across all lessons (predict output, complexity, spot the bug). 8/10 passes; otherwise name the lessons to reread and retest those only. Then he starts at #88 Merge Sorted Array.

## When he reports a problem

He solves on his iPad and reports later from his computer, so the check happens hours after solving. That delay is fine; it tests retention. Always ask which day he solved it and pass `--date` to `new`.

1. **Get the code.** Ask him to paste it (copy from his LeetCode submission) or push it. Note whether he used a hint, the editorial, or AI help at any point; if so, status is `assisted`. No judgement, but it must be recorded.
2. **Scaffold it** (skip if the folder exists):
   ```
   python3 scripts/tracker.py new <id> "<Title>" --difficulty <Easy|Medium|Hard> \
       --category "<study-plan section>" --pattern "<pattern>" [--status assisted] --date <YYYY-MM-DD>
   ```
   Put his code in `solution.<ext>` exactly as written. Do not "clean it up".
3. **Run the comprehension check** (below).
4. **Write NOTES.md** from his answers, in his words where possible. Every section filled. "What tripped me up" is the most valuable section: record real mistakes, not generic advice.
5. **Log it:** `python3 scripts/tracker.py log <id> --confidence <1-5> [--note "..."]`
6. **Rebuild and push:** `python3 scripts/tracker.py build`, then commit `Add #<id> <title>` and push to `main`.
7. Tell him the confidence score, the one gap that cost him points, and when it comes back.

## The comprehension check

Ask in rounds, not one wall of questions. Round 1 is always these three:

1. **Explain it.** "Walk me through your approach in plain English, like I can't see the code."
2. **Why it's correct.** "What is true at every step of your loop?" (the invariant). "Why does that guarantee the right answer?"
3. **Complexity.** "Time and space, and point to the line that causes each."

Round 2: pick two or three based on where round 1 was weak.

4. **Trace it.** Give a small input he hasn't seen, including an edge case, and have him trace the variables step by step.
5. **Break it.** "What input breaks a naive version of this?" or point at a specific line: "What happens if this were `<` instead of `<=`?"
6. **Recognize it.** "What in the problem statement told you to use this pattern?" This is the question that matters most for new problems in an interview.
7. **Alternatives.** "What's the brute force? What's a different approach, and what does it trade?"
8. **Variant.** Change one constraint (unsorted input, allow k duplicates, stream instead of array, return indices instead of values) and ask how the solution changes.

### Scoring

| Confidence | Meaning |
|---|---|
| 5 | Explained, proved, traced, and handled a variant without help. Could teach it. |
| 4 | Solid, one small gap that he fixed himself once pointed at it. |
| 3 | Gets the approach but shaky on why it works or on edge cases. |
| 2 | Can describe what the code does but not why; needed real help on round 1. |
| 1 | Could not explain it. Treat as not solved. |

Claude assigns the score from the answers, not from how confident he sounds. `assisted` problems cap at 3 on the first check.

## Cold re-solves

`python3 scripts/tracker.py due` lists what's due. A re-solve means a blank editor, no looking at the old solution, timed. Afterward, run a shorter check (questions 1, 6, and one variant), then:

```
python3 scripts/tracker.py log <id> --confidence <1-5> --review [--note "..."]
```

At the start of a session, if anything is due, say so before he starts something new. Due re-solves come first.

## Weekly review (Sunday)

1. `python3 scripts/tracker.py week` generates `weekly/YYYY-Www.md`.
2. Ask him the five reflection questions in that file, fill in his answers under Reflection, and push back on vague ones ("I need to practice more" is not a focus).
3. Pick next week's focus: usually the weakest pattern or the category he's been avoiding.
4. Update `PATTERNS.md` with anything new he learned about a pattern.
5. `build`, commit `Week YYYY-Www review`, push.

## Conventions

- Python only. If code arrives in another language, ask him to redo it in Python.
- Folder: `problems/NNNN-slug/` with `solution.<ext>` and `NOTES.md`. The slug matches the LeetCode URL.
- `category` is the Top Interview 150 section (see `CATEGORIES` in `scripts/tracker.py`); use `Other` for problems outside the plan. `pattern` is the technique, which can differ from the category (Remove Element sits in Array / String but its pattern is two pointers).
- Never edit the front matter's dates or confidence by hand; use `log` so the schedule stays consistent.
- README.md is generated. Edit `scripts/tracker.py` to change it, not the README.
