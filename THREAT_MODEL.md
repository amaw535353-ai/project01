# Threat model

## Scope, assets, and actors
Assets are instruction integrity, synthetic marker confidentiality, mock records, tool authorization, response integrity, and audit evidence. Actors are a curious learner, malicious user, malicious document author, and fallible model. There are no external targets.

## Entry points and data flows
HTTP message/mode/approval fields and local document contents enter the orchestration pipeline. Retrieved text and user input are **untrusted**. Model proposals and output are also **untrusted**. Configuration, policy code, tool registry, and test oracle are **trusted for this lab**. Mock records are trusted data but access-controlled.

## Trust boundaries / attack surfaces
User→API, documents→retriever, context→model, model→policy, policy→tools, and output→caller are boundaries. Surfaces include role override text, instruction-like documents, leakage requests, crafted tool proposals, weak approval, and unsafe rendering.

## Threats and mitigations
| Threat | Consequence | Mitigations | Residual risk |
|---|---|---|---|
| Direct/indirect injection | instruction corruption | separation, detection, least privilege | novel wording bypasses detection |
| Leakage | synthetic marker disclosure | keep data out where possible, redaction | transformations may evade redaction |
| RAG poisoning | document becomes authority | trust metadata, suspicious-content classification, isolation | trusted sources may be compromised |
| Tool/agency abuse | unauthorized simulated action | external policy, schemas, approval, deny default | policy bugs and confused deputy |
| Output manipulation | unsafe downstream use | structured validation/redaction | semantic unsafe content |
| Logging exposure | secrets in evidence | synthetic data and minimal events | future fields could add sensitive data |

## Assumptions
Repository and policy code are not attacker-writable at runtime; approval is authentic in the exercise; tools remain mocks; the marker is not valuable. Availability and multi-tenant isolation are out of scope.

This is a qualitative educational model, not proof of security. Revisit boundaries when adding a provider, vector database, identity, or real tool.
