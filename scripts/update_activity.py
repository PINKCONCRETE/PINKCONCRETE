from pathlib import Path
import re,json,urllib.request,os
p=Path(__file__).resolve().parents[1]
user=os.environ.get('PROFILE_USER','PINKCONCRETE')
req=urllib.request.Request(f'https://github.com/users/{user}/contributions',headers={'User-Agent':'profile-contribution-renderer'})
s=urllib.request.urlopen(req,timeout=30).read().decode()
days=[]
for tag in re.findall(r'<td[^>]+data-date[^>]+>',s):
 a=dict(re.findall(r'([\w-]+)="([^"]*)"',tag));days.append({'date':a['data-date'],'level':int(a['data-level'])})
assert len(days)>350,'Incomplete contribution calendar; retaining previous asset'
days.sort(key=lambda d:d['date']);(p/'contributions.json').write_text(json.dumps(days,indent=2))
