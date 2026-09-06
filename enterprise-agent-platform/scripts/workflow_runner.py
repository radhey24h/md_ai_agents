"""Simulate the feature-development workflow with HITL gates.

No third-party packages. Python 3.10+.

  py -3 scripts/workflow_runner.py start --feature customer-notification
  py -3 scripts/workflow_runner.py run
  py -3 scripts/workflow_runner.py approve --by "jane" --comment "Looks good"
  py -3 scripts/workflow_runner.py reject --by "jane" --comment "Missing SLA"
  py -3 scripts/workflow_runner.py status
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "artifacts" / "runs"
ACTIVE = ROOT / "artifacts" / "active-run.json"

STAGES = [
    {
        "id": "requirements",
        "type": "agent",
        "agent": "requirements",
        "model": "high-reasoning",
        "next": "approval-requirements",
    },
    {
        "id": "approval-requirements",
        "type": "hitl",
        "gate": "requirements",
        "approved": "architecture",
        "rejected": "requirements",
    },
    {
        "id": "architecture",
        "type": "agent",
        "agent": "architect",
        "model": "high-reasoning",
        "next": "approval-design",
    },
    {
        "id": "approval-design",
        "type": "hitl",
        "gate": "design",
        "approved": "implementation",
        "rejected": "architecture",
    },
    {
        "id": "implementation",
        "type": "agent",
        "agent": "developer",
        "model": "coding",
        "next": "qa",
    },
    {"id": "qa", "type": "agent", "agent": "qa-reviewer", "model": "high-reasoning", "next": "security"},
    {
        "id": "security",
        "type": "agent",
        "agent": "security-reviewer",
        "model": "high-reasoning",
        "next": "approval-release",
    },
    {
        "id": "approval-release",
        "type": "hitl",
        "gate": "release",
        "approved": "completed",
        "rejected": "implementation",
    },
    {"id": "completed", "type": "terminal"},
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stage_by_id(stage_id: str) -> dict:
    for stage in STAGES:
        if stage["id"] == stage_id:
            return stage
    raise SystemExit(f"Unknown stage: {stage_id}")


def run_dir(feature: str) -> Path:
    return RUNS / feature


def state_path(feature: str) -> Path:
    return run_dir(feature) / "state.json"


def load_state(feature: str) -> dict:
    path = state_path(feature)
    if not path.exists():
        raise SystemExit(f"No run for '{feature}'. Start one first.")
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    path = state_path(state["featureId"])
    path.parent.mkdir(parents=True, exist_ok=True)
    (path.parent / "approvals").mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    ACTIVE.write_text(json.dumps({"featureId": state["featureId"]}, indent=2) + "\n", encoding="utf-8")


def current_feature(cli_feature: str | None) -> str:
    if cli_feature:
        return cli_feature
    if ACTIVE.exists():
        return json.loads(ACTIVE.read_text(encoding="utf-8"))["featureId"]
    raise SystemExit("Pass --feature or start a run first.")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def simulate_agent(state: dict, stage: dict) -> dict:
    feature = state["featureId"]
    agent = stage["agent"]
    base = {
        "workflowId": state["workflowId"],
        "featureId": feature,
        "agent": agent,
        "model": stage.get("model", "unspecified"),
        "status": "PASS",
        "timestamp": now(),
        "nextStage": stage["next"],
        "risks": [],
        "unknowns": [],
        "evidence": [f"Simulated {agent} stage for {feature}."],
    }

    if agent == "requirements":
        payload = {
            **base,
            "summary": "Customer can view and update notification preferences per channel.",
            "functionalRequirements": [
                "Customer can read current email, SMS, and push preferences.",
                "Customer can update marketing vs transactional flags per channel.",
                "Unauthorized users cannot change another customer's preferences.",
            ],
            "businessRules": [
                "Marketing requires explicit opt-in.",
                "Transactional email defaults to on.",
                "Changes apply to future sends only.",
            ],
            "acceptanceCriteria": [
                "GET returns the stored preference document.",
                "PUT persists flags and locale.",
                "PUT by another user returns 403.",
            ],
            "unknowns": ["Is push available on web, or mobile only?"],
        }
        write_json(run_dir(feature) / "requirements.json", payload)
        return payload

    if agent == "architect":
        payload = {
            **base,
            "summary": "customer-service owns preferences; notification-service consumes events.",
            "apiDesign": [
                "GET /customers/{id}/notification-preferences",
                "PUT /customers/{id}/notification-preferences",
            ],
            "dataChanges": ["customer_notification_preferences table in customer-service"],
            "serviceBoundaries": ["customer-service owns data", "notification-service consumes events"],
            "events": ["CustomerNotificationPreferencesChanged"],
            "failureHandling": ["Invalid locale → 400", "Unauthorized → 403"],
            "security": ["Authn required", "Authz: self only"],
            "scalability": ["Single-row per customer; cache-friendly reads"],
            "acceptanceMap": ["GET/PUT cover listed acceptance criteria"],
        }
        write_json(run_dir(feature) / "design.json", payload)
        return payload

    if agent == "developer":
        payload = {
            **base,
            "summary": "Simulated implementation of approved notification-preferences APIs.",
            "implemented": {"backend": True, "frontend": True, "database": True},
            "filesChanged": [
                "src/CustomerService/NotificationPreferencesController.cs",
                "src/Web/notification-preferences.component.ts",
            ],
            "tests": {"unit": 8, "integration": 3},
            "knownGaps": ["Push on web still UNKNOWN pending product."],
        }
        write_json(run_dir(feature) / "implementation.json", payload)
        return payload

    if agent == "qa-reviewer":
        payload = {
            **base,
            "summary": "Acceptance criteria covered by simulated tests.",
            "verdict": "PASS",
            "functional": "PASS",
            "apiContract": "PASS",
            "regression": "PASS",
            "defects": [],
        }
        write_json(run_dir(feature) / "qa.json", payload)
        return payload

    if agent == "security-reviewer":
        payload = {
            **base,
            "summary": "No open high/critical findings in simulation.",
            "findings": [],
            "release_allowed": True,
        }
        write_json(run_dir(feature) / "security.json", payload)
        return payload

    raise SystemExit(f"No simulator for agent {agent}")


def cmd_start(feature: str) -> None:
    state = {
        "workflowId": f"FEAT-{feature}",
        "workflow": "feature-development",
        "featureId": feature,
        "currentStage": "requirements",
        "status": "RUNNING",
        "completedStages": [],
        "gates": {
            "requirements": "pending",
            "design": "pending",
            "release": "pending",
        },
        "history": [{"at": now(), "event": "started"}],
    }
    save_state(state)
    print(f"Started run '{feature}'. Next: py -3 scripts/workflow_runner.py run")


def cmd_status(feature: str) -> None:
    state = load_state(feature)
    stage = stage_by_id(state["currentStage"])
    print(json.dumps({**state, "stageType": stage["type"]}, indent=2))
    if stage["type"] == "hitl":
        print(
            f"\nHITL GATE '{stage['gate']}' is waiting. "
            f"Approve or reject before the workflow can continue."
        )
    elif stage["type"] == "terminal":
        print("\nWorkflow is complete.")
    else:
        print(f"\nNext agent: {stage.get('agent')}. Run: py -3 scripts/workflow_runner.py run")


def cmd_run(feature: str) -> None:
    state = load_state(feature)
    stage = stage_by_id(state["currentStage"])

    if stage["type"] == "terminal":
        print("Already completed.")
        return

    if stage["type"] == "hitl":
        print(
            f"Stopped at HITL gate '{stage['gate']}'.\n"
            f"  py -3 scripts/workflow_runner.py approve --by \"you\" --comment \"ok\"\n"
            f"  py -3 scripts/workflow_runner.py reject --by \"you\" --comment \"reason\""
        )
        return

    result = simulate_agent(state, stage)
    state["completedStages"].append(stage["id"])
    state["currentStage"] = stage["next"]
    state["history"].append(
        {"at": now(), "event": "agent_completed", "agent": stage["agent"], "artifactStatus": result["status"]}
    )
    save_state(state)
    print(
        f"Agent '{stage['agent']}' (model: {stage.get('model', 'unspecified')}) "
        f"wrote artifact. Current stage: {state['currentStage']}"
    )
    if stage_by_id(state["currentStage"])["type"] == "hitl":
        print("HITL required. Workflow will not continue until a human approves or rejects.")


def cmd_decide(feature: str, decision: str, by: str, comment: str) -> None:
    state = load_state(feature)
    stage = stage_by_id(state["currentStage"])
    if stage["type"] != "hitl":
        raise SystemExit(f"Current stage '{stage['id']}' is not a HITL gate.")

    gate = stage["gate"]
    if decision == "approved" and gate == "release":
        qa = json.loads((run_dir(feature) / "qa.json").read_text(encoding="utf-8"))
        security = json.loads((run_dir(feature) / "security.json").read_text(encoding="utf-8"))
        if qa.get("verdict") == "FAIL" or security.get("release_allowed") is False:
            raise SystemExit("Release cannot be approved: QA FAIL or security release_allowed is false.")

    payload = {
        "gate": gate,
        "status": decision,
        "approved_by" if decision == "approved" else "rejected_by": by,
        "timestamp": now(),
        "comments": comment,
    }
    write_json(run_dir(feature) / "approvals" / f"{gate}.json", payload)

    next_id = stage[decision]
    state["gates"][gate] = decision
    state["currentStage"] = next_id
    state["history"].append({"at": now(), "event": decision, "gate": gate, "by": by, "comment": comment})
    if next_id == "completed":
        state["status"] = "PASS"
    save_state(state)
    print(f"Gate '{gate}' {decision}. Next stage: {next_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="HITL feature-development workflow runner")
    sub = parser.add_subparsers(dest="command", required=True)

    start = sub.add_parser("start", help="Create a new feature run")
    start.add_argument("--feature", required=True)

    for name in ("run", "status"):
        p = sub.add_parser(name)
        p.add_argument("--feature")

    for name in ("approve", "reject"):
        p = sub.add_parser(name)
        p.add_argument("--feature")
        p.add_argument("--by", required=True)
        p.add_argument("--comment", default="")

    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "start":
        cmd_start(args.feature)
        return 0

    feature = current_feature(getattr(args, "feature", None))
    if args.command == "run":
        cmd_run(feature)
    elif args.command == "status":
        cmd_status(feature)
    elif args.command == "approve":
        cmd_decide(feature, "approved", args.by, args.comment)
    elif args.command == "reject":
        cmd_decide(feature, "rejected", args.by, args.comment)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
