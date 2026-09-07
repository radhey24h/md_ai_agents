# Walkthrough — Session 07

The orchestrator is a traffic cop, not a superhero developer. Open `agents/orchestrator.md` next to `agents/developer.md`. Even if the orchestrator used the strongest model, it still should not get deploy permission. Model size is not privilege.

After implementation, QA and security can work in parallel, then join, then a human. Run:

```powershell
cd sessions/session-07-multi-agent
py -3 run_multi.py
```

The script writes discovery and requirements artifacts, then **stops** until you treat a human as having approved. Developer must not write `qa.json`. Separate files, separate agents. Writer is not the judge.

Re-run with `--approve-demo` only in class, and say out loud that this flag stands in for a person:

```powershell
py -3 run_multi.py --approve-demo
```

You should then see design, implementation, QA, security, and a join file.

Session 08 is the same story labeled as one enterprise teaching run, with every gate named.
