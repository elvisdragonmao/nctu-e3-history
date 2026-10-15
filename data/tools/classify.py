import json,sys,re,os,glob
out=sys.argv[1]; R=json.load(open(out+'/result.json'))['probe']
SIG={'moodle':r'moodle|M\.cfg|theme/(boost|dcpc|classic)|yui_combo','ecampus':r'ecampus|e-campus|3probe|三趨','eeclass':r'ee-?class|formosasoft|旭聯|wisdom ?master|tronclass|智園|blackboard|canvas lms|open edx|edx',
'platform':r'數位教學平台|數位學習平台|網路教學平台|線上學習系統|網路校園|教學平台|學習平台','ocw':r'開放式課程|opencourseware|\bocw\b',
'oldlink':r'(e3|e3new|e2|dcpc|eportfolio|ocw|e)\.nctu\.edu\.tw|e3\.ym\.edu\.tw|newe3\.ym|ecampus\.ym'}
rows=[]
for h,p in R.items():
    for sch in ('https','http'):
        fn=f"{out}/body/{h}_{sch}.html"
        if not os.path.exists(fn) or p[sch]['code'] in ('','000'): continue
        b=open(fn,'rb').read(600000)
        try: t=b.decode('utf-8')
        except: t=b.decode('big5','ignore')
        hits={k:sorted(set(m.lower() for m in re.findall(v,t,re.I)))[:6] for k,v in SIG.items()}
        hits={k:v for k,v in hits.items() if v}
        tt=p[sch]['title']
        if re.search(r'學習|課程|教學|course|learn|moodle|e3|campus|ocw|portfolio',tt,re.I): hits['title']=[tt]
        if hits: rows.append((h,p[sch]['code'],p[sch]['url'],tt,hits))
        break
strong=[r for r in rows if set(r[4])&{'moodle','ecampus','eeclass','platform','ocw'} or 'title' in r[4]]
for h,c,u,t,hi in sorted(strong): print(h,c,u,'|',t[:60],'|',{k:v for k,v in hi.items() if k!='title'})
print('\n--- pages linking to old hosts ---')
for h,c,u,t,hi in sorted(rows):
    if 'oldlink' in hi: print(h,'|',t[:50],'|',hi['oldlink'])
