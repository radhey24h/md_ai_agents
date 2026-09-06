"""Classroom enterprise path. Independent teaching runtime — not a vendor platform clone."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ART = ROOT / "artifacts"
APP = ROOT / "approvals"
ORDER = [
    "discovery",
    "approval-discovery",
    "requirements",
    "approval-requirements",
    "architecture",
    "approval-design",
    "implementation",
    "qa_security",
    "approval-release",
    "release",
    "completed",
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load() -> dict:
    p = ART / "state.json"
    if not p.exists():
        raise SystemExit("start first")
    return json.loads(p.read_text(encoding="utf-8"))


def save(s: dict) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    APP.mkdir(parents=True, exist_ok=True)
    (ART / "state.json").write_text(json.dumps(s, indent=2) + "\n", encoding="utf-8")


def dump(name: str, **kw) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    body = {"feature": "customer-notification", "status": "PASS", "unknowns": ["SMS"], **kw}
    (ART / name).write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")


def _reset_json(folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    for p in folder.glob("*.json"):
        if p.name != ".gitkeep.json":
            p.unlink()


def cmd_start() -> None:
    _reset_json(ART)
    _reset_json(APP)
    save({"current": "discovery"})
    print("Started. Next: run (parallel discovery)")


def cmd_status() -> None:
    print(json.dumps(load(), indent=2))


def cmd_run() -> None:
    s = load()
    cur = s["current"]
    if cur.startswith("approval-"):
        print(f"STOPPED HITL {cur}. Human: approve --gate ...")
        return
    if cur == "discovery":
        for n in ("api-analysis.json", "db-analysis.json", "ui-analysis.json"):
            dump(n, branch=n)
        dump("consolidated-discovery.json", join=True)
        s["current"] = "approval-discovery"
        save(s)
        print("Discovery joined. STOP HITL discovery")
        return
    if cur == "requirements":
        dump(
            "requirements.json",
            facts=["Email notification can be enabled or disabled.", "Preference belongs to the customer."],
            evidence=["examples/customer-notification/business-rules.md"],
            inferences=["GET /customers/{id} is used to load the preference owner."],
            unknowns=["SMS"],
        )
        s["current"] = "approval-requirements"
        save(s)
        print("Requirements written. STOP HITL requirements")
        return
    if cur == "architecture":
        dump("design.json", note="email-only")
        s["current"] = "approval-design"
        save(s)
        print("Design written. STOP HITL design")
        return
    if cur == "implementation":
        dump("implementation.json", note="simulated implementation")
        s["current"] = "qa_security"
        save(s)
        print("Implementation recorded. Next run is QA || security")
        return
    if cur == "qa_security":
        dump("qa.json", verdict="PASS")
        dump("security.json", release_allowed=True)
        s["current"] = "approval-release"
        save(s)
        print("QA || security joined. STOP HITL release")
        return
    if cur == "release":
        dump("release.json", note="teaching complete")
        s["current"] = "completed"
        save(s)
        print("Release recorded. completed")
        return
    print("Already completed." if cur == "completed" else f"state={cur}")


def cmd_approve(gate: str, by: str) -> None:
    s = load()
    expected = {
        "discovery": "approval-discovery",
        "requirements": "approval-requirements",
        "design": "approval-design",
        "release": "approval-release",
    }[gate]
    if s["current"] != expected:
        raise SystemExit(f"Not at {expected} (now {s['current']})")
    APP.mkdir(parents=True, exist_ok=True)
    (APP / f"{gate}.json").write_text(
        json.dumps({"gate": gate, "status": "approved", "by": by, "at": now()}, indent=2) + "\n",
        encoding="utf-8",
    )
    nxt = {
        "discovery": "requirements",
        "requirements": "architecture",
        "design": "implementation",
        "release": "release",
    }[gate]
    s["current"] = nxt
    save(s)
    print(f"Approved {gate}. Next: {nxt}")


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("start")
    sub.add_parser("run")
    sub.add_parser("status")
    a = sub.add_parser("approve")
    a.add_argument("--gate", required=True, choices=["discovery", "requirements", "design", "release"])
    a.add_argument("--by", required=True)
    args = p.parse_args()
    if args.cmd == "start":
        cmd_start()
    elif args.cmd == "run":
        cmd_run()
    elif args.cmd == "status":
        cmd_status()
    else:
        cmd_approve(args.gate, args.by)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
