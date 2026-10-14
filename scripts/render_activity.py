from pathlib import Path
import json,datetime,html
p=Path(__file__).resolve().parents[1]
days=json.loads((p/'contributions.json').read_text())
start=datetime.date.fromisoformat(days[0]['date']);end=datetime.date.fromisoformat(days[-1]['date'])
colors=['#202729','#3f5049','#607760','#91a77e','#c2d7a4']
b='<rect width="1000" height="260" fill="#101315"/><path d="M32 1H968" stroke="#303637"/>'
def t(x,y,s,size=11,color='#89918e'):return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{html.escape(s)}</text>'
b+=t(32,34,'ACTIVITY / PUBLIC CONTRIBUTION RECORD')+t(703,34,str(start)+' — '+str(end),10)
b+=t(32,75,'A year of building.',26,'#e6e7e3')
prev=None
for d in days:
 dt=datetime.date.fromisoformat(d['date']);delta=(dt-start).days;col=delta//7;row=(dt.weekday()+1)%7;x=71+col*16;y=117+row*14
 if dt.month!=prev and dt.day<8:b+=t(x,106,dt.strftime('%b'),9);prev=dt.month
 b+=f'<rect class="cell" x="{x}" y="{y}" width="11" height="10" rx="1" fill="{colors[d["level"]]}" style="animation-delay:{col*.055:.3f}s"><title>{d["date"]}: GitHub contribution intensity {d["level"]}/4</title></rect>'
b+='<g class="sweep"><rect x="70" y="114" width="1" height="103" fill="#c2d7a4" opacity=".65"/></g>'
b+=t(32,244,'PINKCONCRETE / GITHUB',9)+t(660,244,'Less',9)
for i,c in enumerate(colors):b+=f'<rect x="{699+i*16}" y="235" width="11" height="10" rx="1" fill="{c}"/>'
b+=t(788,244,'More',9)+t(863,244,'UPDATED '+str(end),8)
style='text{font-family:Menlo,Consolas,monospace}.cell{animation:appear 12s ease infinite}.sweep{animation:scan 12s linear infinite}@keyframes appear{0%,3%{opacity:.18}25%,100%{opacity:1}}@keyframes scan{from{transform:translateX(0)}to{transform:translateX(850px)}}@media(prefers-reduced-motion:reduce){.cell,.sweep{animation:none}.sweep{display:none}}'
(p/'assets/activity.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="260" viewBox="0 0 1000 260" role="img" aria-label="GitHub contribution calendar"><title>Real GitHub contributions — animated reveal</title><style>{style}</style>{b}</svg>')
