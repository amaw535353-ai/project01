from dataclasses import dataclass
from pathlib import Path

@dataclass
class Document:
    name: str
    text: str
    trust: str

def retrieve(query: str, root: Path = Path("documents")) -> list[Document]:
    words = set(query.lower().split())
    docs = []
    for path in root.glob("*/*.txt"):
        text = path.read_text()
        score = len(words & set(text.lower().split()))
        if score or "policy" in query.lower():
            docs.append(Document(str(path), text, path.parent.name))
    return docs[:3]
