#!/usr/bin/env python3
"""DNS-resolve a host list, then GET http:// and https:// root of each live host.
Usage: probe.py names.txt outdir"""
import sys, socket, subprocess, json, re, os, html
from concurrent.futures import ThreadPoolExecutor
names=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out=sys.argv[2]; os.makedirs(out+'/body',exist_ok=True)
KW=re.compile(r'e3|moodle|數位教學|數位學習|教學平台|網路校園|e-?campus|e-?learning|\blms\b|wisdom ?master|旭聯|blackboard|開放式課程|opencourse|ocw|教材|dcpc|課程網|course',re.I)
def dns(h):
    try: return h, sorted({a[4][0] for a in socket.getaddrinfo(h,None,socket.AF_INET)})
    except Exception as e: return h, None
def get(h, scheme):
    fn=f"{out}/body/{h}_{scheme}.html"
    r=subprocess.run(['curl','-s','-k','-L','--max-redirs','5','-m','12','--connect-timeout','6','-A','Mozilla/5.0 (history research)',
        '-o',fn,'-w','%{http_code}\t%{url_effective}\t%{size_download}',f'{scheme}://{h}/'],capture_output=True,text=True)
    code,url,size=(r.stdout.split('\t')+['','',''])[:3]
    title=''; kws=[]; meta=''
    try:
        b=open(fn,'rb').read(400000)
        for enc in ('utf-8','big5','cp950','latin-1'):
            try: t=b.decode(enc); break
            except: pass
        m=re.search(r'<title[^>]*>(.*?)</title>',t,re.S|re.I); title=html.unescape(m.group(1)).strip()[:120] if m else ''
        m=re.search(r'http-equiv=["\']?refresh["\']?[^>]*url=([^"\'>]+)',t,re.I); meta=m.group(1) if m else ''
        kws=sorted({k.lower() for k in KW.findall(t)})[:15]
    except FileNotFoundError: pass
    return dict(code=code,url=url,size=size,title=title,refresh=meta,kw=kws)
with ThreadPoolExecutor(64) as ex: res=dict(ex.map(dns,names))
alive=[h for h,a in res.items() if a]
print(f'{len(names)} names, {len(alive)} resolve',file=sys.stderr)
def probe(h): return h,{'ip':res[h],'http':get(h,'http'),'https':get(h,'https')}
with ThreadPoolExecutor(24) as ex: pr=dict(ex.map(probe,alive))
json.dump({'dns':res,'probe':pr},open(out+'/result.json','w'),ensure_ascii=False,indent=1)
with open(out+'/summary.tsv','w') as f:
    f.write('host\tip\thttp_code\thttps_code\tfinal_url\ttitle\trefresh\tkeywords\n')
    for h,p in sorted(pr.items()):
        best=p['https'] if p['https']['code'] not in ('','000') else p['http']
        f.write('\t'.join([h,','.join(p['ip']),p['http']['code'],p['https']['code'],best['url'],best['title'].replace('\t',' ').replace('\n',' '),best['refresh'],','.join(best['kw'])])+'\n')
