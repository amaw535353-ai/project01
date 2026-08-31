# Attack analysis

Each category below uses the mandatory **What → Why → Where → How → When → Defense → Verification → Residual risk** lens. Individual machine-readable cases live under `attacks/`.

## Direct injection and prompt leakage
**WHAT:** Input requests role override or hidden prompt/token disclosure. **WHY:** Vulnerable mode confuses user data with authority and embeds a synthetic marker in its system text. **WHERE:** `Lab.run` vulnerable branch. **HOW:** suspicious language activates deterministic mock leakage. **WHEN:** untrusted messages influence completion without an enforceable boundary. **DEFENSE:** avoid secrets in prompts, classify, isolate, redact, and minimize capabilities. **VERIFICATION:** integration leakage tests and the `PI`/`PL` evaluation cases. **RESIDUAL RISK:** classifiers and literal redaction can be bypassed; provider prompts may leak.

## Indirect injection and RAG poisoning
**WHAT:** A retrieved local file tells the model to disclose or act. **WHY:** retrieval relevance does not confer instruction authority. **WHERE:** `documents/malicious` → `rag.retrieve` → orchestration context. **HOW:** an ordinary policy query retrieves adversarial text. **WHEN:** retrieved text is interpreted as instructions. **DEFENSE:** source/trust labels, detection, contextual isolation, access control, and capability limits. **VERIFICATION:** `II`/`RP` cases produce contained or blocked outcomes in hardened mode. **RESIDUAL RISK:** trusted documents can be compromised and semantic detectors miss obfuscation.

## Tool manipulation and excessive agency
**WHAT:** Attacker text induces a privileged mock action. **WHY:** vulnerable mode treats model selection as authorization. **WHERE:** `_proposal` and vulnerable `tools.execute` call. **HOW:** tool-like language creates a proposal. **WHEN:** model output directly invokes broad capabilities. **DEFENSE:** external deny-by-default policy, scoped roles, argument validation, explicit approval, and simulated tools. **VERIFICATION:** policy unit tests and unauthorized-tool security test. **RESIDUAL RISK:** authorization logic, identity, or argument validation can contain defects.

## Output manipulation
**WHAT:** Attack attempts to make protected material appear in output. **WHY:** downstream callers may trust fluent model text. **WHERE:** response construction. **HOW:** leakage request or malicious context influences response. **WHEN:** output is rendered/executed without validation. **DEFENSE:** schema, redaction, safe rendering, and never executing prose. **VERIFICATION:** hardened leakage regression test. **RESIDUAL RISK:** encoding and semantic transformation evade literal rules.
