"""Where am I in the primer? Run: python progress.py  (or Terminal > Run Task > Primer progress)

Runs every exercise file quietly and shows how many tests pass in each lesson,
then tells you exactly what to open next."""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EX = HERE / "exercises"

LESSONS = [
    ("01", "Basics", "01-basics.md", "ex01_basics.py", "Tue"),
    ("02", "Lists", "02-lists.md", "ex02_lists.py", "Tue"),
    ("03", "Strings", "03-strings.md", "ex03_strings.py", "Wed"),
    ("04", "Dicts and sets", "04-dicts-sets.md", "ex04_dicts_sets.py", "Wed"),
    ("05", "deque, heapq, bisect", "05-deque-heap-bisect.md", "ex05_deque_heap_bisect.py", "Wed"),
    ("06", "Recursion and classes", "06-functions-recursion-classes.md", "ex06_functions_recursion.py", "Thu"),
    ("07", "Built-ins, math, bits", "07-builtins-math-bits.md", "ex07_builtins_math_bits.py", "Thu"),
    ("08", "Gotchas (fix the bugs)", "08-complexity-gotchas.md", "ex08_gotchas.py", "Thu"),
]
SUMMARY = re.compile(r"(\d+)/(\d+) passing, (\d+) failing, (\d+) not started")


def status(exercise: str) -> tuple[int, int, int, int]:
    out = subprocess.run([sys.executable, exercise], cwd=EX, capture_output=True, text=True).stdout
    m = SUMMARY.search(out)
    return tuple(map(int, m.groups())) if m else (0, 0, 0, 0)


def main() -> None:
    print(f"\n  {'':3} {'Lesson':<28} {'Day':<5} {'Tests':<7} Status")
    print("  " + "-" * 60)
    next_up = None
    total_ok = total = 0
    for num, name, notes, ex, day in LESSONS:
        ok, n, failing, todo = status(ex)
        total_ok += ok
        total += n
        if n and ok == n:
            mark, state = "[x]", "done"
        elif ok or failing:
            mark, state = "[~]", f"{failing} failing, {todo} not started"
        else:
            mark, state = "[ ]", "not started"
        if next_up is None and not (n and ok == n):
            next_up = (num, name, notes, ex, ok or failing)
        print(f"  {mark:3} {num} {name:<25} {day:<5} {ok:>2}/{n:<4} {state}")
    print("  " + "-" * 60)
    print(f"  {total_ok}/{total} tests passing overall\n")

    if next_up is None:
        print("  All lessons pass. Tell Claude you're ready for the exit test.\n")
        return
    num, name, notes, ex, started = next_up
    print(f"  NEXT: lesson {num}, {name}")
    if not started:
        print(f"    1. Read   python-primer/{notes}  (opens formatted)")
        print(f"    2. Answer the 'Predict the output' questions before opening the answers")
        print(f"    3. Open   python-primer/exercises/{ex}  and press Ctrl+Shift+B to run its tests")
    else:
        print(f"    Keep going in python-primer/exercises/{ex}, Ctrl+Shift+B to rerun the tests")
    print(f"    When it's all ok: push, then tell Claude \"lesson {num} done\"\n")


if __name__ == "__main__":
    main()
