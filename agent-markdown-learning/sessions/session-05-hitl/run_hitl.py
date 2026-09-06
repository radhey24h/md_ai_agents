"""Teaching runtime: HITL stop. Not an IDE. Approve is a CLI act, not a model act."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ART = ROOT / "artifacts"
APP = ROOT / "approvals"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def state_path() -> Path:
    return ART / "state.json"


def load() -> dict:
    if not state_path().exists():
        raise SystemExit("Run: py -3 run_hitl.py start")
    return json.loads(state_path().read_text(encoding="utf-8"))


def save(state: dict) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    APP.mkdir(parents=True, exist_ok=True)
    state_path().write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def cmd_start() -> None:
    save({"current": "requirements", "feature": "customer-notification"})
    print("Started. Next: py -3 run_hitl.py run")


def cmd_run() -> None:
    state = load()
    cur = state["current"]
    if cur == "requirements":
        ART.mkdir(parents=True, exist_ok=True)
        (ART / "requirements.json").write_text(
            json.dumps({"feature": "customer-notification", "status": "PASS", "unknowns": ["SMS"]}, indent=2)
            + "\n",
            encoding="utf-8",
        )
        state["current"] = "approval-requirements"
        save(state)
        print("Wrote requirements.json. STOP: HITL gate approval-requirements")
        return
    if cur == "approval-requirements":
        print("STOPPED at HITL. A human must: approve or reject. The model must not do this.")
        return
    if cur == "architecture":
        (ART / "design.json").write_text(
            json.dumps({"feature": "customer-notification", "status": "PASS", "note": "email-only design"}, indent=2)
            + "\n",
            encoding="utf-8",
        )
        state["current"] = "completed"
        save(state)
        print("Architect ran. Completed teaching path.")
        return
    print("Already completed." if cur == "completed" else f"Unknown stage {cur}")


def cmd_decide(decision: str, by: str, comment: str) -> None:
    state = load()
    if state["current"] != "approval-requirements":
        raise SystemExit("Not at a HITL gate.")
    APP.mkdir(parents=True, exist_ok=True)
    payload = {"gate": "requirements", "status": decision, "by": by, "comment": comment, "at": now()}
    (APP / "requirements.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    state["current"] = "architecture" if decision == "approved" else "requirements"
    save(state)
    print(f"Gate {decision}. Next stage: {state['current']}")


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("start")
    sub.add_parser("run")
    for name in ("approve", "reject"):
        x = sub.add_parser(name)
        x.add_argument("--by", required=True)
        x.add_argument("--comment", default="")
    args = p.parse_args()
    if args.cmd == "start":
        cmd_start()
    elif args.cmd == "run":
        cmd_run()
    elif args.cmd == "approve":
        cmd_decide("approved", args.by, args.comment)
    else:
        cmd_decide("rejected", args.by, args.comment)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
