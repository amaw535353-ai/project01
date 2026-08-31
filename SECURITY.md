# Security and safe use

This repository intentionally contains vulnerable code and the fake marker `LAB_ONLY_7421`. Run it only as a local authorized lab. Tools perform no network or durable side effects; records are fictional. Never add credentials, customer data, outbound messaging, shell tools, or production authorization. Bind to localhost unless the Codespace port is private.

Report accidental real-secret commits privately to the repository owner, revoke the credential, and rewrite history where appropriate. Vulnerable mode is expected to fail security properties. Hardened mode demonstrates risk reduction, not immunity.
