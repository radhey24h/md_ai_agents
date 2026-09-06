"""Teaching runtime for multi-agent shape. --approve-demo is a classroom stand-in for a human."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ART = Path(__file__).resolve().parent / "artifacts"


def w(name: str, **kw) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    (ART / name).write_text(json.dumps({"feature": "customer-notification", "status": "PASS", **kw}, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    for n in ("api-analysis.json", "db-analysis.json", "ui-analysis.json"):
        w(n, branch=n)
    w("requirements.json", unknowns=["SMS"])
    if argv[1:] != ["--approve-demo"]:
        print("STOP (teaching HITL). Re-run with --approve-demo only after you explain a human approved.")
        return 0
    w("design.json", note="email-only")
    w("implementation.json", note="simulated")
    w("qa.json", verdict="PASS")
    w("security.json", release_allowed=True)
    w("join.json", from_=["qa.json", "security.json"])
    print("Classroom path completed after simulated human approvals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
