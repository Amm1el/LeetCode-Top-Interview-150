"""Run a lesson notebook's setup, exercise and test cells without Jupyter and print
one summary line. Used by progress.py. Usage: python run_notebook.py 01-basics.ipynb"""
import contextlib
import io
import json
import os
import sys
from pathlib import Path

RUN_TAGS = {"setup", "exercise", "test"}


def main(path: str) -> None:
    nb_path = Path(path).resolve()
    os.chdir(nb_path.parent)
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    env = {"__name__": "__main__"}
    for cell in nb["cells"]:
        if cell["cell_type"] != "code" or not RUN_TAGS & set(cell.get("metadata", {}).get("tags", [])):
            continue
        src = "".join(cell["source"])
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            try:
                exec(compile(src, "<cell>", "exec"), env)
            except BaseException:
                pass
    results = sys.modules["check"].RESULTS if "check" in sys.modules else {}
    vals = list(results.values())
    ok, todo = vals.count("ok"), vals.count("TODO")
    print(f"{ok}/{len(vals)} passing, {len(vals) - ok - todo} failing, {todo} not started")


if __name__ == "__main__":
    main(sys.argv[1])
