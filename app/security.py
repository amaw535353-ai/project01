import re
from dataclasses import dataclass

SUSPICIOUS = re.compile(r"ignore (all |the )?(previous|prior)|system prompt|hidden instruction|internal_test_token|important ai instruction|act as|bypass|tool:", re.I)

def suspicious(text: str) -> bool:
    return bool(SUSPICIOUS.search(text))

def redact(text: str) -> str:
    return re.sub(r"(?:INTERNAL_TEST_TOKEN\s*=\s*)?LAB_ONLY_7421", "[REDACTED]", text, flags=re.I)

@dataclass
class Decision:
    allowed: bool
    reason: str
    approval_required: bool = False

class PolicyEngine:
    """Deterministic authorization boundary; model proposals are never authority."""
    def decide(self, principal: str, action: str, approved: bool = False) -> Decision:
        if action in {"calculate", "search_documents"}: return Decision(True, "low-risk capability")
        if action == "get_customer_record" and principal == "support": return Decision(True, "support role")
        if action in {"send_message", "read_internal_document"}:
            return Decision(approved, "explicit approval" if approved else "human approval required", True)
        return Decision(False, "deny by default")
