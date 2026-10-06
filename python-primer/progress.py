"""Where am I in the primer? Terminal > Run Task > Primer progress  (or: python progress.py)

Runs the exercise and test cells of every lesson notebook quietly, shows how many
tests pass in each lesson, then tells you exactly what to open next."""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNNER = HERE / "_primer" / "run_notebook.py"

LESSONS = [
    ("01", "Basics", "01-basics.ipynb", "Tue"),
    ("02", "Lists", "02-lists.ipynb", "Tue"),
    ("03", "Strings", "03-strings.ipynb", "Wed"),
    ("04", "Dicts and sets", "04-dicts-sets.ipynb", "Wed"),
    ("05", "deque, heapq, bisect", "05-deque-heap-bisect.ipynb", "Wed"),
    ("06", "Recursion and classes", "06-functions-recursion-classes.ipynb", "Thu"),
    ("07", "Built-ins, math, bits", "07-builtins-math-bits.ipynb", "Thu"),
    ("08", "Gotchas (fix the bugs)", "08-complexity-gotchas.ipynb", "Thu"),
]
SUMMARY = re.compile(r"(\d+)/(\d+) passing, (\d+) failing, (\d+) not started")


def status(notebook: str) -> tuple[int, int, int, int]:
    try:
        out = subprocess.run([sys.executable, str(RUNNER), str(HERE / notebook)],
                             capture_output=True, text=True, timeout=60).stdout
    except subprocess.TimeoutExpired:
        return (0, 0, 0, 0)       # something in the notebook loops forever
    m = SUMMARY.search(out)
    return tuple(map(int, m.groups())) if m else (0, 0, 0, 0)


def main() -> None:
    print(f"\n  {'':3} {'Lesson':<28} {'Day':<5} {'Tests':<7} Status")
    print("  " + "-" * 60)
    next_up = None
    total_ok = total = 0
    for num, name, nb, day in LESSONS:
        ok, n, failing, todo = status(nb)
        total_ok += ok
        total += n
        if n and ok == n:
            mark, state = "[x]", "done"
        elif ok or failing:
            mark, state = "[~]", f"{failing} failing, {todo} not started"
        else:
            mark, state = "[ ]", "not started"
        if next_up is None and not (n and ok == n):
            next_up = (num, name, nb, ok or failing)
        print(f"  {mark:3} {num} {name:<25} {day:<5} {ok:>2}/{n:<4} {state}")
    print("  " + "-" * 60)
    print(f"  {total_ok}/{total} tests passing overall\n")

    if next_up is None:
        print("  All lessons pass. Tell Claude you're ready for the exit test.\n")
        return
    num, name, nb, started = next_up
    print(f"  NEXT: lesson {num}, {name}")
    if not started:
        print(f"    Open python-primer/{nb} and work top to bottom (Shift+Enter runs a cell).")
    else:
        print(f"    Keep going in python-primer/{nb}: finish the exercises and rerun their check cells.")
    print(f"    Save the notebook (Ctrl+S) so this command sees your work.")
    print(f"    When it's all ok: commit and sync, then tell Claude \"lesson {num} done\"\n")


if __name__ == "__main__":
    main()
