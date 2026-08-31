from app.lab import Lab
from app.models import ChatRequest

lab=Lab()
try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    app=FastAPI(title="Prompt Injection Defense Lab")
    class Request(BaseModel):
        message: str; mode: str="hardened"; use_rag: bool=True; approved: bool=False; principal: str="learner"
    @app.post("/chat")
    def chat(request: Request): return lab.run(ChatRequest(**request.model_dump())).dict()
    @app.get("/health")
    def health(): return {"status":"ok"}
except ImportError:
    app=None
