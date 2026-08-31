# Prompt Injection Attack & Defense Lab

A safe, local, deterministic lab for observing how attacker-controlled instructions cross LLM application trust boundaries. It contrasts **vulnerable**, **basic**, and **hardened** modes against the same 40-case suite. All records, tools, tokens, and side effects are synthetic. Prompt injection is not “solved”; the hardened design contains impact by treating model output as untrusted.

## Security objectives
Protect instruction integrity, the synthetic `LAB_ONLY_7421` marker, tool authorization, and response integrity while preserving benign functionality. The lab covers direct/indirect injection, leakage, RAG poisoning, tool manipulation, and excessive agency.

## Architecture
`POST /chat` → classification → local retrieval → mock-model behavior → proposed tool → deterministic policy → simulated tool → output validation. See [ARCHITECTURE.md](ARCHITECTURE.md), [THREAT_MODEL.md](THREAT_MODEL.md), and [CODE_MAP.md](CODE_MAP.md).

## Reproduce
```bash
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
pytest
rm -f evidence/security-events.jsonl
for mode in vulnerable basic hardened; do python -m evaluations.run --mode "$mode" > /dev/null; done
python scripts/compare.py
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Then POST JSON such as `{"message":"Summarize policy","mode":"hardened"}` to `/chat`. No provider key or network service is needed.

## Evaluation methodology and results
An attack is **successful** only when the deterministic oracle observes simulated leakage, poisoned-instruction influence, or a proposed unauthorized action in vulnerable mode. **Blocked** means rejected; **contained** means untrusted content reached retrieval but did not cause a protected effect. Defense success is `(blocked + contained) / total`. False positives are deliberately `null`, not invented, until a labeled benign evaluation dataset exists. Measured results are regenerated in `evidence/`; see [EVALUATION.md](EVALUATION.md).

## Key lessons, limitations, residual risks
Prompt text is not authorization. Separate instructions from data, constrain capabilities, authorize outside the model, validate output, and retain correlated evidence. Detection is heuristic and bypassable; the mock model is deterministic and unlike a production model; retrieval is intentionally simple; approvals are simulated; and no real provider is included. See [LESSONS_LEARNED.md](LESSONS_LEARNED.md) and [SECURITY.md](SECURITY.md).

## Study path
Start with `app/lab.py`, then `app/security.py`, `app/rag.py`, `app/tools.py`, the attack dataset, and tests. Continue with [STUDY_GUIDE.md](STUDY_GUIDE.md). This is an authorized educational environment—not a production security control.
