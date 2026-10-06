"""Test helper for the primer notebooks. Standard library only.

In a notebook:
    lesson("ex01_basics")    # once, in the setup cell
    check("reverse_int")     # after an exercise cell: runs tests/test_ex01_basics.py::test_reverse_int
    summary()                # end of the notebook: every result so far
"""
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
_state = {"lesson": None}
RESULTS: dict[str, str] = {}


def eq(got, expected, msg=""):
    assert got == expected, f"{msg + ': ' if msg else ''}expected {expected!r}, got {got!r}"


def lesson(name: str) -> None:
    _state["lesson"] = name
    RESULTS.clear()
    print(f"Ready: {name}. Run each cell in order with Shift+Enter.")


def _load_tests(namespace: dict) -> dict:
    src = (HERE / "tests" / f"test_{_state['lesson']}.py").read_text(encoding="utf-8")
    env = dict(namespace)          # tests see whatever the notebook has defined so far
    exec(compile(src, f"test_{_state['lesson']}.py", "exec"), env)
    return env


def check(name: str) -> None:
    caller = sys._getframe(1).f_globals
    env = _load_tests(caller)
    test = env.get(f"test_{name}")
    if test is None:
        print(f"No test named {name!r}.")
        return
    try:
        test()
    except NotImplementedError:
        RESULTS[name] = "TODO"
        print(f"TODO  {name}: replace `raise NotImplementedError` with your code, then rerun both cells")
    except AssertionError as e:
        RESULTS[name] = "FAIL"
        print(f"FAIL  {name}: {e}" if str(e) else f"FAIL  {name}")
    except Exception:
        RESULTS[name] = "ERROR"
        last = traceback.format_exc().strip().splitlines()[-1]
        print(f"ERROR {name}: {last}")
    else:
        RESULTS[name] = "ok"
        print(f"ok    {name}")


def summary() -> None:
    if not RESULTS:
        print("No tests run yet. Use Run All (top of the notebook), then run this cell again.")
        return
    for name, status in RESULTS.items():
        print(f"  {status:<5} {name}")
    ok = sum(s == "ok" for s in RESULTS.values())
    print(f"\n{ok}/{len(RESULTS)} passing")
    if ok == len(RESULTS):
        print("All done. Fill in 'My traps' below, commit and sync, then tell Claude the lesson is done.")
