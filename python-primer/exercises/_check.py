"""Tiny test runner for the primer exercises. Standard library only.

Each exercise file ends with:
    if __name__ == "__main__":
        from _check import run
        run(globals())

and defines test_* functions. Run a file with `python3 ex01_basics.py`.
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
