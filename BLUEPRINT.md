# AI Security Engineer 2026+ Blueprint

**Repository:** `amaw535353-ai/project01`  
**Blueprint date:** 2026-08-31  
**Goal:** become demonstrably job-ready for AI Security Engineering across LLM/application security, agent security, adversarial ML, secure MLOps/supply chain, red teaming/evaluation, architecture, and governance.

This is a **gate-based blueprint**, not a deadline-based curriculum. Advance when evidence shows competence. Build, attack, defend, measure, explain, and preserve reproducible evidence.

---

## 1. Starting point: what Project 01 already proves

Project 01 is already a useful first portfolio artifact rather than a toy README-only project.

It currently demonstrates:

- direct and indirect prompt-injection scenarios;
- RAG poisoning and untrusted-document handling;
- synthetic sensitive-information leakage;
- tool manipulation and excessive-agency scenarios;
- vulnerable, basic, and hardened execution modes;
- deterministic authorization outside the model;
- output redaction/validation;
- correlated JSONL security-event logging;
- a 40-case adversarial evaluation set;
- unit, integration, and adversarial tests;
- GitHub Actions CI;
- reproducible local execution without a real provider key.

See [README.md](README.md), [ARCHITECTURE.md](ARCHITECTURE.md), [EVALUATION.md](EVALUATION.md), [THREAT_MODEL.md](THREAT_MODEL.md), and [STUDY_GUIDE.md](STUDY_GUIDE.md).

### Current architectural lesson

The strongest design idea in this repo is the separation between **model proposal** and **trusted authorization**. The model may suggest a tool action, but `PolicyEngine` decides whether it is permitted. Preserve this principle in every future agentic project: **LLM output is untrusted input, not authority**.

### Important current gaps

Project 01 intentionally documents several limitations that should become the next engineering targets:

1. The attack dataset cannot measure false positives because there is no labeled benign evaluation dataset.
2. Prompt-injection detection is a small regex heuristic and should never be treated as a security boundary.
3. Approval is represented as a boolean rather than an authenticated, scoped, expiring approval object.
4. Tool authorization is coarse-grained and does not deeply validate arguments, resources, purpose, or tenant boundaries.
5. Retrieval is intentionally simple and does not model realistic vector/embedding controls.
6. The mock model is deterministic and does not test provider/model variability.
7. CI proves tests and one hardened evaluation run, but it is not yet a complete software/AI supply-chain security pipeline.
8. The lab does not yet model MCP, agent memory, inter-agent communication, delegated identity, or cascading agent failures.

These are not reasons to discard Project 01. They are the roadmap for turning it into a stronger portfolio artifact.

---

## 2. 2026+ reference frameworks

Use current authoritative frameworks as a shared vocabulary, not as checklists to memorize.

### Primary AI-security references

- **OWASP GenAI LLM Top 10 2026** — current LLM/GenAI application risks and mitigations:  
  https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- **OWASP Top 10 for Agentic Applications 2026** — autonomous/tool-using agent risks:  
  https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **MITRE ATLAS** — adversary tactics, techniques, mitigations, and case studies for AI-enabled systems:  
  https://atlas.mitre.org/
- **NIST AI RMF Generative AI Profile (NIST AI 600-1)** — lifecycle risk-management guidance for generative AI:  
  https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

### Supporting software-security references

- **OWASP ASVS** — application security verification requirements:  
  https://owasp.org/www-project-application-security-verification-standard/
- **OWASP API Security Top 10** — API authorization, resource access, abuse, and inventory risks:  
  https://owasp.org/API-Security/
- **OpenSSF Scorecard** — measurable open-source/supply-chain security checks:  
  https://openssf.org/scorecard/

When standards change, update this file and record the review date in git history.

---

## 3. Target competency model

A job-ready AI Security Engineer should be able to work across eight connected domains.

### Domain A — Security foundations

Required capability:

- Linux, processes, files, permissions, networking, DNS, TLS, HTTP;
- Python and secure coding;
- authentication, authorization, sessions, secrets, cryptography basics;
- common web/API vulnerabilities;
- threat modeling and abuse cases;
- logging, detection, incident response, and evidence handling.

Evidence standard:

- build and secure a small API;
- identify trust boundaries;
- reproduce at least several common web/API flaws in authorized labs;
- write regression tests that prove the fixes.

### Domain B — ML and data foundations

Required capability:

- supervised/unsupervised learning concepts;
- train/validation/test separation;
- metrics, overfitting, calibration, and distribution shift;
- embeddings, similarity search, retrieval, ranking;
- model artifacts, datasets, preprocessing, and inference pipelines;
- basic PyTorch or equivalent model workflows.

Evidence standard:

- train/evaluate a small model;
- explain its data flow and failure modes;
- implement a reproducible evaluation pipeline;
- distinguish model-quality metrics from security metrics.

### Domain C — Adversarial ML

Required capability:

- evasion, poisoning, backdoors, model extraction, membership/privacy risks;
- adversarial examples and robustness evaluation;
- attack preconditions and attacker capabilities;
- realistic defense limitations.

Evidence standard:

- build a small authorized adversarial-ML lab;
- implement at least one attack and one mitigation;
- compare clean accuracy and robustness metrics;
- document assumptions and residual risk.

### Domain D — LLM, RAG, and application security

Required capability:

- direct/indirect prompt injection;
- sensitive-information disclosure;
- system-prompt exposure limits;
- insecure output handling;
- vector/embedding and retrieval weaknesses;
- RAG poisoning;
- unbounded consumption and cost/availability controls;
- authorization outside the LLM.

Evidence standard:

- Project 01 plus the hardening gates in Section 5;
- reproducible attack datasets;
- benign utility dataset;
- measured attack success, containment, and false-positive/utility metrics.

### Domain E — Agent, MCP, and tool security

Required capability:

- goal hijacking;
- tool misuse;
- identity and privilege abuse;
- agentic supply-chain risks;
- unexpected code execution;
- memory/context poisoning;
- insecure inter-agent communication;
- cascading failures;
- human-agent trust exploitation;
- least privilege and capability design for tools/MCP servers.

Evidence standard:

- a local agent lab where the model can propose actions but cannot independently authorize protected effects;
- scoped identities and tool permissions;
- expiring approvals;
- attack simulations for poisoned memory, malicious tool metadata, and privilege escalation;
- auditable policy decisions.

### Domain F — AI red teaming and security evaluation

Required capability:

- threat-led test design;
- attack taxonomy mapping;
- deterministic and probabilistic evaluation;
- mutation/fuzz testing;
- multi-turn attacks;
- canary/synthetic-secret testing;
- pass/fail oracles;
- defense regression testing;
- reproducible reporting.

Evidence standard:

- create an evaluation harness that runs attacks across multiple model/configuration variants;
- store per-case evidence;
- distinguish exploitability from model misbehavior;
- report uncertainty and avoid invented metrics.

### Domain G — Secure MLOps and AI supply chain

Required capability:

- CI/CD security;
- dependency and container security;
- model/dataset provenance;
- artifact integrity;
- secret management;
- least-privilege deployment identities;
- environment separation;
- rollback and incident response;
- secure inference configuration;
- monitoring for abuse, cost, and anomalous tool use.

Evidence standard:

- build a pipeline that tests, scans, packages, produces an SBOM, records provenance, deploys a constrained service, and preserves evidence;
- demonstrate a supply-chain failure and the control that blocks/detects it.

### Domain H — Architecture, governance, and communication

Required capability:

- AI threat modeling;
- risk acceptance and residual-risk documentation;
- mapping technical controls to NIST/OWASP/MITRE;
- security requirements and design reviews;
- incident playbooks;
- communicating risk to engineers and leadership without overstating guarantees.

Evidence standard:

- architecture diagram;
- trust-boundary analysis;
- threat model;
- security requirements;
- control-to-risk mapping;
- executive summary that accurately states limitations.

---

## 4. Portfolio ladder

Do not build ten shallow repos. Build a smaller set of projects that each prove a distinct hiring signal.

### Project 01 — Prompt Injection Attack & Defense Lab

**Status:** existing foundation.

Primary signals:

- LLM application threat modeling;
- prompt-injection/RAG/tool risks;
- deterministic policy enforcement;
- adversarial evaluation;
- security logging.

Next objective: complete the Project 01 hardening gates in Section 5.

### Project 02 — Secure RAG and Retrieval Security Lab

Build a realistic local retrieval service with:

- embedding generation;
- vector store;
- document ingestion pipeline;
- source/tenant metadata;
- ACL-aware retrieval;
- provenance and trust labels;
- poisoned and benign corpus;
- retrieval-specific adversarial evaluation.

Attack scenarios:

- poisoned chunks;
- cross-tenant retrieval;
- metadata spoofing;
- hidden instructions;
- embedding collision/semantic manipulation experiments;
- sensitive-document retrieval;
- malicious document updates.

Required evidence:

- retrieval precision/utility metrics;
- attack success rate;
- false-positive/false-block rate;
- per-document provenance;
- tenant-isolation tests.

### Project 03 — Agent/MCP Security Gateway

Build a local agent that can access several synthetic tools through a gateway.

Security architecture must include:

- authenticated principal;
- explicit tool allowlist;
- argument schema validation;
- resource-level authorization;
- capability scoping;
- expiring approval object;
- rate/cost limits;
- side-effect preview;
- policy decision log;
- deny-by-default behavior.

Attack scenarios:

- malicious tool descriptions;
- goal hijacking;
- tool argument injection;
- delegated-identity abuse;
- memory poisoning;
- privilege escalation;
- confused-deputy behavior;
- inter-agent message spoofing.

### Project 04 — Adversarial ML Service

Build and expose a small classifier through an API.

Security work:

- baseline clean evaluation;
- evasion attack;
- poisoning or backdoor experiment in a controlled dataset;
- robustness evaluation;
- model artifact hashing/provenance;
- rate limiting and inference abuse controls;
- model-extraction threat analysis.

The goal is not to claim a universal adversarial defense. The goal is to demonstrate attacker-model reasoning, measurement, and control tradeoffs.

### Project 05 — Secure AI Supply Chain / MLOps Pipeline

Build a CI/CD path for one of the earlier projects.

Minimum controls:

- pinned dependencies;
- dependency vulnerability checks;
- static analysis;
- secret scanning;
- container build;
- non-root runtime;
- SBOM generation;
- artifact/model hashes;
- provenance record;
- protected deployment environment;
- least-privilege runtime identity;
- rollback instructions.

Add one controlled supply-chain failure and prove the pipeline detects or blocks it.

### Project 06 — AI Red-Team & Evaluation Harness

Create a reusable local framework that can test multiple targets/configurations.

Capabilities:

- dataset schema;
- attack taxonomy tags;
- multi-turn cases;
- deterministic oracles where possible;
- model-graded results only when clearly separated from hard oracles;
- repeated trials for nondeterministic targets;
- confidence/variance reporting;
- benign utility dataset;
- regression thresholds;
- HTML/Markdown evidence report.

Map scenarios to OWASP GenAI 2026 and MITRE ATLAS.

### Project 07 — Capstone: Secure Enterprise AI Assistant

Integrate:

- authenticated API;
- ACL-aware RAG;
- agent/tool gateway;
- policy engine;
- secure approvals;
- telemetry;
- abuse/cost controls;
- supply-chain pipeline;
- adversarial evaluation;
- incident playbook;
- NIST/OWASP/MITRE mapping.

The capstone should include both a **red-team report** and a **defender remediation report** against the same system.

---

## 5. Project 01 hardening gates

These are the next engineering gates for this repository.

### Gate P01-1 — Benign utility and false-positive evaluation

Add a labeled benign dataset covering normal summaries, RAG questions, calculator use, support-record access, and approved tool actions.

Required metrics:

- benign pass rate;
- false-positive/block rate;
- attack success rate;
- defense success/containment rate;
- per-category counts.

Pass condition:

- metrics are generated from executed cases, not inferred;
- every metric has a reproducible denominator;
- CI fails on a defined security or utility regression threshold.

### Gate P01-2 — Replace boolean approval with a scoped approval object

Replace `approved: bool` with an approval object containing at minimum:

- approval ID;
- authenticated principal/approver;
- permitted action;
- permitted resource or argument constraints;
- issue time;
- expiry time;
- nonce or replay protection;
- integrity protection or trusted-server lookup.

Pass condition:

- expired, replayed, wrong-action, wrong-principal, and modified approvals are rejected by tests.

### Gate P01-3 — Resource- and argument-aware authorization

Change policy from mostly action-level decisions to decisions over:

`principal + action + resource + arguments + context + approval`

Pass condition:

- tests prove that an allowed tool name cannot be abused with unauthorized arguments or resources;
- deny-by-default remains explicit.

### Gate P01-4 — Structured tool proposal validation

Validate every model-proposed tool call against a strict schema before policy evaluation.

Pass condition:

- malformed, extra-field, type-confused, and oversized arguments are rejected;
- no string-built command execution is introduced.

### Gate P01-5 — Retrieval trust and provenance

Extend document metadata to include source identity, trust level, provenance, and tenant/security scope.

Pass condition:

- trust metadata cannot silently convert attacker-controlled content into authority;
- tests cover forged/mislabeled metadata;
- retrieval decisions are logged.

### Gate P01-6 — Output contracts instead of redaction-only defense

Keep redaction as defense in depth, but add a structured output contract for sensitive flows.

Pass condition:

- protected data is omitted by construction where possible;
- encoded/fragmented synthetic secret cases are included in regression tests;
- documentation explicitly states redaction is bypassable.

### Gate P01-7 — CI security baseline

Extend GitHub Actions to include appropriate code/dependency/container checks and generate reproducible evidence artifacts.

Pass condition:

- tests run on pull requests;
- dependency/security checks are automated;
- hardened and benign evaluation thresholds are enforced;
- generated evidence is traceable to a commit SHA.

### Gate P01-8 — Agentic extension

Add a local agent/tool mode that models at least:

- goal hijacking;
- malicious tool metadata;
- memory/context poisoning;
- delegated privilege misuse.

Pass condition:

- protected actions remain controlled by deterministic authorization outside the LLM;
- scenarios map to OWASP Agentic Top 10 2026 categories;
- evidence shows attack behavior before and after controls.

---

## 6. Study/practice order

Use this sequence because later AI-security work depends on earlier security and ML understanding.

1. Linux, networking, HTTP, Python, Git, testing
2. Web/API security and authorization
3. Threat modeling and secure architecture
4. ML fundamentals and evaluation
5. Adversarial ML fundamentals
6. LLM application security
7. RAG/vector security
8. Agent/MCP security
9. AI red teaming and evaluation engineering
10. Secure MLOps and AI supply chain
11. Detection, monitoring, and incident response for AI systems
12. Governance/risk mapping and security communication
13. Integrated capstone

---

## 7. Challenge operating model

For each substantive challenge:

1. State the threat/security objective.
2. Predict the result before running the experiment.
3. Make the smallest defensible change.
4. Run the test/evaluation.
5. Preserve commands, diff, logs, and measured result.
6. Explain why the control works and where it can fail.
7. Restore or commit a clean final state.
8. Do not advance until the evidence demonstrates the target competency.

Suggested scoring gate:

- **80/100 minimum to pass a substantive challenge**;
- below 80: remediate and resubmit;
- preserve both first-attempt and current score for progress evidence.

---

## 8. Job-readiness evidence checklist

Do not use course completion as the final signal. Use demonstrated engineering evidence.

You are approaching job readiness when you can independently:

- threat-model an AI application and identify trust boundaries;
- distinguish model behavior from application authorization;
- secure an LLM/RAG/agent application against realistic abuse paths;
- design least-privilege tool and identity boundaries;
- test direct and indirect prompt injection;
- test RAG poisoning and retrieval isolation;
- test agent memory/tool/identity attacks;
- implement adversarial-ML experiments and explain their assumptions;
- build a security evaluation harness with reproducible metrics;
- add CI/CD and supply-chain controls for AI artifacts;
- investigate AI security events using correlated telemetry;
- write actionable findings with severity, exploit path, evidence, remediation, and residual risk;
- map technical risks to OWASP GenAI, OWASP Agentic, MITRE ATLAS, and NIST AI RMF without pretending a mapping itself proves security;
- explain limitations clearly to both engineers and non-engineers.

A strong portfolio should show **before/after evidence**: exploitable or unsafe baseline, implemented control, regression test, measured delta, and honest residual risk.

---

## 9. What not to optimize for

Avoid these traps:

- collecting certifications without building systems;
- treating prompt filtering as a complete prompt-injection defense;
- treating system prompts as secrets or policy enforcement;
- using an LLM to authorize its own privileged actions;
- reporting attack-only success rates as if they measure benign usability;
- claiming a defense is complete because a small handcrafted dataset passes;
- connecting training labs to real destructive tools or production credentials;
- building many shallow demos without tests, threat models, and evidence;
- memorizing framework names without being able to implement controls.

---

## 10. Immediate next action

The next best engineering step in this repository is **Gate P01-1: add a labeled benign evaluation dataset and compute utility/false-positive metrics alongside the existing 40-case attack suite**.

Why this is first:

- the current evaluation explicitly leaves false positives as `null`;
- security controls that block everything can look deceptively strong on attack-only data;
- adding benign evaluation creates the measurement foundation needed before making more aggressive defenses.

The implementation should remain local, reproducible, synthetic, and provider-independent.

---

## 11. Definition of success for this blueprint

This blueprint succeeds only if it produces verifiable engineering evidence over time.

The end state is not “knows AI security terminology.” The end state is:

> Can design, build, attack, defend, evaluate, monitor, and explain AI-enabled systems while preserving strong software-security boundaries around probabilistic model behavior.

Update this blueprint as the ecosystem changes, but keep that engineering standard constant.
