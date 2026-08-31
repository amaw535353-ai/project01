from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass
class ChatRequest:
    message: str
    mode: str = "hardened"
    use_rag: bool = True
    approved: bool = False
    principal: str = "learner"

@dataclass
class ToolProposal:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)

@dataclass
class ChatResponse:
    request_id: str
    mode: str
    answer: str
    outcome: str
    events: list[dict[str, Any]]
    tool_result: Any = None

    def dict(self): return asdict(self)
