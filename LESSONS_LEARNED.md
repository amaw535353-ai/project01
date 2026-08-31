# Lessons learned

* Model instructions cannot enforce authorization against attacker-influenced model output.
* Retrieved relevance is not trust; documents are data even when they contain imperative prose.
* Detection is useful telemetry but brittle as a primary control.
* Least privilege, deterministic policy, validation, and approval contain consequences when injection succeeds.
* Evaluation labels must describe observable protected effects, and false positives require benign data.
* This mock makes paths reproducible but cannot estimate production-model behavior. Future work: labeled benign corpus, authenticated approvals, richer argument schemas, provider adapter, HTML UI, and verified standards links.
