#!/bin/bash
# Pull host names for *.nycu/nctu/ym.edu.tw from Common Crawl indexes, with retries.
S=$1; cd "$S" || exit 1
fetch(){ # url outfile
  for i in 1 2 3 4 5 6; do
    curl -s -m 120 "$1" -o "$2.tmp"
    if head -c 20 "$2.tmp" | grep -q '^{'; then mv "$2.tmp" "$2"; return 0; fi
    sleep $((i*10))
  done; rm -f "$2.tmp"; return 1; }
for c in $(cat cc_pick.txt); do for d in nycu.edu.tw nctu.edu.tw ym.edu.tw; do
  case "$c" in CC-MAIN-20{08,09,12,13,14,15,16,17,18,19}*) [ $d = nycu.edu.tw ] && continue;; esac
  np=""; fetch "https://index.commoncrawl.org/$c-index?url=*.$d&showNumPages=true" np_$c_$d.json && np=$(python3 -I -c "import json,sys;print(json.load(open(sys.argv[1]))['pages'])" np_$c_$d.json 2>/dev/null)
  [ -z "$np" ] && { echo "FAIL pages $c $d"; continue; }
  for ((p=0;p<np;p++)); do
    fetch "https://index.commoncrawl.org/$c-index?url=*.$d&output=json&fl=url&page=$p" cc_${c}_${d}_$p.jsonl || echo "FAIL $c $d page $p"
  done; echo "done $c $d pages=$np"
done; done
cat cc_*.jsonl 2>/dev/null | grep -o '"url": *"[^"]*"' | sed -E 's#.*://([^/:"]+).*#\1#' | tr A-Z a-z | sort -u > cc_hosts.txt
wc -l cc_hosts.txt
