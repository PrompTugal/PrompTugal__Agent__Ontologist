import json
rows={"a-voz-do-algarve":"geral@avozdoalgarve.pt","barlavento":"info@barlavento.pt","correio-alentejo":"geral@correioalentejo.com"}
for i,m in rows.items():
    p=f'data/organisations/{i}/organisation.json';raw=open(p).read();d=json.loads(raw)
    ind=2 if raw.startswith('{\n  "') else 4
    c=d['media']['contact'];c['official_email']=m
    c['source']['read_at']='2026-11-26'; c['source']['how']="the outlet's own contact page, read by cl-6.researcher and re-read by cl-6.security on 26 Nov 2026; a role mailbox only"
    open(p,'w').write(json.dumps(d,indent=ind,ensure_ascii=False)+"\n")
