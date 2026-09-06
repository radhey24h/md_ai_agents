"""Teaching runtime: sequential stages only. Not an IDE."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ART = ROOT / "artifacts"
ORDER = ["requirements", "architecture", "implementation", "qa"]
FILES = {
    "requirements": "requirements.json",
    "architecture": "design.json",
    "implementation": "implementation.json",
    "qa": "qa.json",
}


def load_state() -> dict:
    path = ART / "state.json"
    if not path.exists():
        return {"current": "requirements", "completed": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    (ART / "state.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def write_stage(name: str) -> None:
    payload = {
        "feature": "customer-notification",
        "stage": name,
        "status": "PASS",
        "summary": f"Teaching sample output for {name}.",
    }
    (ART / FILES[name]).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if argv[1:] == ["skip-to-developer"]:
        state = load_state()
        if state["current"] != "implementation":
            print(f"ERROR: cannot run developer; current stage is {state['current']}")
            return 1
        print("Would run developer (already at implementation).")
        return 0

    state = load_state()
    current = state["current"]
    if current == "completed":
        print("Already completed.")
        return 0
    write_stage(current)
    idx = ORDER.index(current)
    state["completed"].append(current)
    state["current"] = ORDER[idx + 1] if idx + 1 < len(ORDER) else "completed"
    save_state(state)
    print(f"Ran {current}. Next: {state['current']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
