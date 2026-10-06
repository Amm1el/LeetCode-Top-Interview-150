"""Tiny test runner for the primer exercises. Standard library only.

Each exercise file ends with run_tests(__file__), which loads tests/test_<name>.py
(those import the exercise file and define test_* functions) and prints ok / FAIL / TODO.
"""
import traceback


def run(namespace: dict) -> None:
    tests = [(name, fn) for name, fn in namespace.items() if name.startswith("test_") and callable(fn)]
    passed = todo = failed = 0
    for name, fn in tests:
        label = name[len("test_"):]
        try:
            fn()
        except NotImplementedError:
            todo += 1
            print(f"  TODO  {label}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {label}: {e}" if str(e) else f"  FAIL  {label}")
        except Exception:
            failed += 1
            print(f"  ERROR {label}:")
            print("        " + traceback.format_exc().strip().splitlines()[-1])
        else:
            passed += 1
            print(f"  ok    {label}")
    print(f"\n{passed}/{len(tests)} passing, {failed} failing, {todo} not started")


def eq(got, expected, msg=""):
    assert got == expected, f"{msg + ': ' if msg else ''}expected {expected!r}, got {got!r}"


def run_tests(exercise_file: str) -> None:
    """Load tests/test_<exercise>.py (which imports the exercise) and run it."""
    import importlib.util
    import sys
    from pathlib import Path

    ex = Path(exercise_file).resolve()
    sys.path.insert(0, str(ex.parent))
    test_path = ex.parent / "tests" / f"test_{ex.stem}.py"
    spec = importlib.util.spec_from_file_location(f"test_{ex.stem}", test_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(f"Testing {ex.name}\n")
    run(vars(mod))
