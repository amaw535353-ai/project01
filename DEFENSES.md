# Defense catalog

| Control | Security property / threat | Location | Assumptions / limitations / bypasses | Tests / evidence |
|---|---|---|---|---|
| Instruction/data separation | document text lacks authority; indirect injection | `app/lab.py`, `app/rag.py` | trust metadata is accurate; compromised trusted sources remain possible | adversarial suite, mode reports |
| Suspicious-content detection | signal direct/leakage attempts | `app/security.py` | heuristic only; paraphrase/encoding bypass and false positives | `test_detection_and_redaction` |
| Least privilege and deny default | unauthorized tools do not run | `PolicyEngine.decide` | principal and approval must be authentic; policy bugs remain | policy positive/negative tests |
| Human approval boundary | sensitive mock actions require consent | `PolicyEngine.decide` | boolean simulates a real workflow; replay is out of scope | `test_approval_allows`, denial test |
| Argument validation | tool input cannot become arbitrary code | `tools.execute` | tiny calculator grammar; business validation remains necessary | unit/integration path |
| Output validation/redaction | marker absent from hardened output | `security.redact`, `Lab.run` | literal redaction is bypassable; do not put secrets in prompts | hardened leakage test |
| Structured audit events | decisions are traceable | `Lab.run.log` | logs omit full content and therefore limit forensics | `evidence/security-events.jsonl` |

No control is claimed to eliminate prompt injection. Impact containment comes from composing independent controls, especially deterministic authorization outside the attacker-influenceable model.

## Standards mapping
Conceptually aligns with OWASP guidance on prompt injection, sensitive information disclosure, excessive agency, and insecure output handling; NIST AI RMF Govern/Map/Measure/Manage functions; and MITRE ATLAS adversarial-ML threat modeling. **TODO:** verify and add current authoritative identifiers/URLs before claiming version-specific mappings. No unverified IDs are asserted here.
