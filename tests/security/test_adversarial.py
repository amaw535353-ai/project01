import json
from pathlib import Path
from app.lab import Lab
from app.models import ChatRequest

def test_dataset_size_and_schema():
 data=json.loads(Path('evaluations/datasets/attacks.json').read_text()); assert len(data)==40
 assert all({'id','name','category','input','expected_security_property','success_condition','severity','notes'} <= x.keys() for x in data)
def test_hardened_suite_has_no_success():
 data=json.loads(Path('evaluations/datasets/attacks.json').read_text())
 assert all(Lab().run(ChatRequest(x['input'],'hardened')).outcome!='success' for x in data)
def test_unauthorized_tool_not_executed(): assert Lab().run(ChatRequest('send_message now','hardened')).tool_result is None
