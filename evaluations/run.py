import argparse, json
from collections import Counter, defaultdict
from pathlib import Path
from app.lab import Lab
from app.models import ChatRequest

def evaluate(mode, output=None):
 attacks=json.loads(Path('evaluations/datasets/attacks.json').read_text())
 lab=Lab(Path('evidence/security-events.jsonl'))
 rows=[]
 for attack in attacks:
  response=lab.run(ChatRequest(attack['input'],mode))
  rows.append({'id':attack['id'],'category':attack['category'],'outcome':response.outcome,'answer':response.answer,'tool_result':response.tool_result})
 counts=Counter(r['outcome'] for r in rows); categories={}
 for category in sorted({r['category'] for r in rows}):
  selected=[r for r in rows if r['category']==category]; c=Counter(r['outcome'] for r in selected)
  categories[category]={'total':len(selected),**c,'attack_success_rate':round(100*c['success']/len(selected),2)}
 report={'mode':mode,'total_attacks':len(rows),'successful_attacks':counts['success'],'blocked_attacks':counts['blocked'],'contained_attacks':counts['contained'],'false_positives':None,'attack_success_rate':round(100*counts['success']/len(rows),2),'defense_success_rate':round(100*(counts['blocked']+counts['contained'])/len(rows),2),'metric_note':'Rates use attack outcomes only; false positives require benign dataset and are not inferred.','by_category':categories,'results':rows}
 path=Path(output or f'evidence/{mode}-results.json'); path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(report,indent=2)+'\n'); return report

def main():
 p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['vulnerable','basic','hardened'],required=True); p.add_argument('--output'); a=p.parse_args(); print(json.dumps(evaluate(a.mode,a.output),indent=2))
if __name__=='__main__': main()
