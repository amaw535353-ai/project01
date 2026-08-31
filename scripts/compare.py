import json
from pathlib import Path
rows=[]
for mode in ('vulnerable','basic','hardened'):
 d=json.loads(Path(f'evidence/{mode}-results.json').read_text()); rows.append((mode,d['total_attacks'],d['successful_attacks'],d['blocked_attacks'],d['contained_attacks'],d['attack_success_rate']))
out=['# Measured comparison','','Generated only from evaluation JSON files.','','| Mode | Total | Successful | Blocked | Contained | Attack success rate |','|---|---:|---:|---:|---:|---:|']
out += [f'| {m} | {t} | {s} | {b} | {c} | {r:.2f}% |' for m,t,s,b,c,r in rows]
Path('evidence/comparison.md').write_text('\n'.join(out)+'\n')
