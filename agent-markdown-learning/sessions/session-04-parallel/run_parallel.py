"""Teaching runtime: parallel fan-out then join."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ART = Path(__file__).resolve().parent / "artifacts"
BRANCHES = ("api-analysis", "db-analysis", "ui-analysis")


def write(name: str, extra: dict | None = None) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    payload = {"feature": "customer-notification", "branch": name, "status": "PASS", **(extra or {})}
    (ART / f"{name}.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if argv[1:] == ["illegal"]:
        print("ERROR: cannot parallelize architecture + developer; developer depends on architecture output.")
        return 1
    for b in BRANCHES:
        write(b, {"note": f"Independent {b} for notification preferences."})
    missing = [b for b in BRANCHES if not (ART / f"{b}.json").exists()]
    if missing:
        print("ERROR: join failed, missing", missing)
        return 1
    write(
        "consolidated-analysis",
        {"inputs": [f"{b}.json" for b in BRANCHES], "unknowns": ["SMS"]},
    )
    print("Fan-out complete. Join wrote consolidated-analysis.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
