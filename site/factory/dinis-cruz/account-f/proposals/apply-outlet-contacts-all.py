# Sets media.contact.official_email on the outlets that publish a role mailbox (cl-6.researcher's batches 1 to 7, read 2026-11-26).
# Run from the website clone: python3 -I apply-outlet-contacts-all.py outlet-contacts-batches-1-to-7-with-mailbox.json
# Keeps the recorded page; first mailbox when an outlet lists two; read_at and how updated. No other field is touched.
import json,sys
for r in json.load(open(sys.argv[1])):
    p=f"data/organisations/{r['id']}/organisation.json";raw=open(p).read();d=json.loads(raw)
    ind=2 if raw.startswith('{\n  "') else 4
    c=d['media'].setdefault('contact',{'page':r['page'],'source':{'url':r['page']}})
    assert c['page']==r['page'],(r['id'],c['page'],r['page'])
    c['official_email']=r['mailbox'][0]
    c['source']['url']=r['page'];c['source']['read_at']=r['read']
    c['source']['how']="the outlet's own contact page, read by cl-6.researcher on 26 Nov 2026 and checked by cl-6.security; a role mailbox only"
    open(p,'w').write(json.dumps(d,indent=ind,ensure_ascii=False)+"\n")
