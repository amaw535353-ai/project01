# Reverse-engineering study guide

## Level 1 — trace
1. Where is user input first typed and where is its correlation ID created?
2. Where does retrieved document text enter orchestration? Which field labels trust?
3. Find the synthetic token. Why is placing a real equivalent here unsafe?
4. Draw the exact vulnerable tool path.

## Level 2 — reason
1. Compare the three branches in `Lab.run`. Which controls prevent impact versus merely detect text?
2. Why can the model propose an action but not authorize it?
3. Which benign test proves hardened mode has not simply stopped all requests?
4. Recalculate one category metric from its per-case rows.

## Level 3 — attack and defend
1. Can you create an injection that avoids `SUSPICIOUS`? Predict each mode before testing.
2. What happens if trust metadata lies? Add a regression test before changing code.
3. Which tool arguments need stronger business validation?
4. Design an authenticated, expiring approval object to replace the boolean.

## Controlled experiments
1. **Authorization:** temporarily bypass `PolicyEngine`; predict, run tool cases, record, restore, compare.
2. **Document trust:** move the malicious file to benign; determine whether path labels alone are relied upon.
3. **Prompt structure:** remove hardened document isolation; run indirect/RAG cases.
4. **Permissions:** allow learners to read records; identify the violated property.
5. **Approval:** change a high-risk action to low risk; test unauthorized execution.
6. **Validation:** remove calculator AST allowlist and explain why arbitrary evaluation becomes dangerous (do not execute malicious payloads).
7. **Retrieval:** change matching/top-k and observe attack exposure versus useful retrieval.
8. **Output:** encode the marker in a mock response; characterize redaction limits and propose schema-level containment.

For every experiment record hypothesis, exact diff, commands, measured delta, conclusion, and restoration commit. Do not connect tools to real systems.
