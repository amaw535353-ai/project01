import ast, operator

CUSTOMERS = {"C-100": {"name": "Ada Example", "tier": "demo"}}

def execute(name, args):
    if name == "calculate":
        tree = ast.parse(str(args.get("expression", "0")), mode="eval")
        allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub)
        if any(not isinstance(n, allowed) for n in ast.walk(tree)): raise ValueError("unsafe expression")
        return eval(compile(tree, "<calculator>", "eval"), {"__builtins__": {}})
    if name == "get_customer_record": return CUSTOMERS.get(args.get("id"), {})
    if name == "send_message": return {"simulated": True, "recipient": args.get("recipient")}
    if name == "read_internal_document": return "Synthetic internal handbook; no real secrets."
    if name == "search_documents": return {"simulated": True, "query": args.get("query")}
    raise ValueError("unknown tool")
