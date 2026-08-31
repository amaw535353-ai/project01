# Code map

| File | Purpose / security relevance | Inputs → outputs | Trust | Main API |
|---|---|---|---|---|
| `app/main.py` | HTTP boundary and shape validation | JSON → response JSON | boundary | `chat`, `health` |
| `app/lab.py` | mode orchestration and instrumentation | request/docs → `ChatResponse` | mixed | `Lab.run`, `_proposal` |
| `app/security.py` | detection, redaction, authorization | text/proposal context → decision | trusted control | `suspicious`, `redact`, `PolicyEngine.decide` |
| `app/rag.py` | transparent local retrieval with trust labels | query/files → documents | output untrusted | `retrieve` |
| `app/tools.py` | strictly local mock capabilities | validated proposal → synthetic result | trusted implementation | `execute` |
| `app/models.py` | internal data contracts | Python values → typed records | neutral | request/response/proposal models |
| `evaluations/run.py` | deterministic adversarial oracle/metrics | dataset+mode → measured JSON | trusted test harness | `evaluate`, `main` |
| `evaluations/datasets/attacks.json` | 40 harmless cases | fixtures | untrusted simulation | JSON records |
| `tests/` | positive, negative, attack, regression checks | code → assertions | verification | pytest tests |
