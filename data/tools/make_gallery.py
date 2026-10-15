#!/usr/bin/env python3
"""Generate gallery.html from images/ with era grouping and captions."""
import os, html, sys
root = sys.argv[1]
C = {
 "e_2000-12_home.png":"E.NCTU V1.0 時期首頁（2000-12，切圖多數未存檔）",
 "e_2001-02_home.png":"E.NCTU 新年版首頁（2001-02）",
 "e_2001-06_home.png":"E.NCTU 首頁與人氣排行榜（2001-06）",
 "e_2002-02_home.png":"E.NCTU 2002 版首頁（Flash 未存檔）",
 "e_2003-12_home.png":"E.NCTU 最後版本首頁（2003-12，只剩兩則公告）",
 "e_2003-12_profile.png":"關於本站 Profile.htm（2003-12）",
 "e_2004-02_teamgroup.png":"E.NCTU 工作團隊（2004-02）",
 "e_2004-02_sitemap.png":"E.NCTU 網站導覽：個人工作室／組織建館（2004-02）",
 "e_2001-06_orglist.png":"組織列表：課程、行政單位、社團（2001-06）",
 "e_2002-04_bbs_phorum.png":"課程討論區 Phorum：Java程式設計（2002-04）",
 "e_2001-03_profile_image001.png":"E.NCTU logo（Profile 頁圖檔）",
 "e_2001-03_profile_functions.jpg":"系統定位圖：人流／知識流／資訊流",
 "e_2001-03_profile_architecture.jpg":"E.NCTU 系統架構：FreeBSD + PHP + PostgreSQL",
 "e_2001-06_header_r01_c01.jpg":"2001 版首頁 banner「e.nctu.edu.tw」",
 "2003_e-nctu_profile_image004.jpg":"E.NCTU 簡報：緣起（87–89 年計畫）",
 "2003_e-nctu_profile_image006.jpg":"E.NCTU 簡報：特點",
 "2003_e-nctu_profile_image010.jpg":"E.NCTU 簡報：系統平台架構",
 "2003_e-nctu_profile_image012.jpg":"網路學習研究中心 logo／聯絡",
 "e2_2002-10_login.png":"e2 eCampus 最早登入頁（2002-10，本機重建）",
 "wayback_2002-10-10_e2_eCampus_login.png":"e2 eCampus 登入頁（2002-10-10，Wayback 渲染）",
 "e2_2003-01_login.png":"e2 eCampus 登入頁（2003-01）",
 "e2_2006-04_login.png":"e2 eCampus 4.0.2005.0217 版登入頁（2006-04，本機重建）",
 "e2_2004-09_course-signup.png":"台灣聯合大學網路教學課程選課登錄系統（e2 主機，2004-09）",
 "e2_2005-06_help_popup.png":"e2 操作說明：設定快顯封鎖（2005-06）",
 "e2_2007-08_dcpc_e2-end-notice.png":"DCPC 公告：E2 服務至九月底止，請轉用 E3（2007-08-16）",
 "wayback_2007-09-11_dcpc_home_E2_end_notice.png":"DCPC 首頁公告列表：E2 停用、e3 同步上線（2007-09）",
 "e2_2002-10_logo.gif":"e2 ecampus logo","e2_2002-10_campus-logo.gif":"e2 交大校徽圖",
 "e2_2006-04_bg_logo.gif":"e2 template_02 logo","e2_2006-04_bg_logo_school.gif":"e2 template_02 校徽",
 "e3_2006-04_login.png":"舊 E3 首版登入頁「網路教學平台 v.3」（2006-04）",
 "wayback_2006-07-03_e3_NCTU_E3_login.png":"舊 E3 登入頁（2006-07）",
 "e3_2006_copyright.gif":"舊 E3 版權圖：版權所有 國立交通大學 ©2006",
 "2006_e3_login_copyright_NCTU.gif":"舊 E3 版權圖（另一份下載）",
 "2007_e3ym_login_copyright_NCTU.gif":"陽明 e3.ym.edu.tw 沿用的同一張交大版權圖（2007）",
 "e3_2007-09_dcpc_portal_home.png":"DCPC 首頁兼 E3 入口，左側 e-Campus 登入框（2007-09）",
 "e3_2009-03_login_E3P.png":"NCTU_E3P 時期登入頁（2009-03，切圖未存檔）",
 "e3_2012-01_dcpc_portal_home.png":"DCPC 首頁 2010 改版，藍色 e-Campus 登入框（2012-01）",
 "e3_2012-06_login_EASY_E3P.png":"NCTU_EASY_E3P 時期登入頁（2012-06）",
 "e3_2016-01_dcpc_portal_home.png":"DCPC 首頁（2016-01）",
 "e3_2018-01_dcpc_portal_home.png":"新舊並行期：New E3 網址公告（2018-01）",
 "2017-09_NewE3_intro_p1.png":"《New E3 數位教學平台介紹》2017/09 版 p.1",
 "2017-09_NewE3_intro_p3.png":"《New E3 數位教學平台介紹》2017/09 版 p.3",
 "e3new_2019-07_login.png":"New e3 登入頁（2019-07，CSS 未存檔）",
 "wayback_2019-11-18_e3new_NewE3_login.png":"New e3 登入頁（2019-11）",
 "wayback_2020-07-16_dcpc_e3_revised_107-2_notice.png":"DCPC：「e3已於107下學期改版」（2020-07）",
 "e3new_2020-11_login.png":"New e3 登入頁完整樣式（2020-11）",
 "logo_e3new_NewE3Cloud_orange_w.png":"New e3 雲朵 logo 原檔",
 "2021-01-28_e3new_maintain.png":"e3new 維護頁：搬家到 e3.nycu 前一天（2021-01-28）",
 "wayback_2021-01-30_e3nycu_login.png":"e3.nycu 首日（2021-01-30）",
 "e3nycu_2021-02_login.png":"e3.nycu 合校初期（2021-02）",
 "e3nycu_2022-12_login.png":"e3.nycu 校外專用登入＋Google Authenticator（2022-12）",
 "2023-09_E3workshop112-1_p7_old_platforms.png":"112-1 工作坊：陽明舊平台 eCampus／eeClass／NewE3(ym)（2023-09）",
 "wayback_2024-04-14_e3p_login.png":"e3p 最早存檔（2024-04-14）",
 "e3p_2024-04_login.png":"e3p 登入頁（2024-04）",
 "e3p_2025-02_login.png":"e3p（Moodle 4.1–4.3 時期，2025-02）",
 "e3p_2026-05_login.png":"e3p（Moodle ≥4.5 時期，2026-05，部分 CSS 未存檔）",
 "live_e3.nycu.edu.tw_2026-10.png":"現況：e3.nycu.edu.tw 登入頁原貌（擋下轉址後截取）",
 "live_e3.nycu.edu.tw_redirected-to-e3p_2026-10.png":"現況：開 e3.nycu 會被轉到 e3p",
 "live_e3p.nycu.edu.tw_2026-10.png":"現況：e3p.nycu.edu.tw",
 "live_eportfolio.nycu.edu.tw_2026-10.png":"現況：eportfolio.nycu.edu.tw",
 "live_ocw.nycu.edu.tw_2026-10.png":"現況：ocw.nycu.edu.tw（仍有交大時期課程）",
 "live_video.ocw.nycu.edu.tw_2026-10.png":"現況：video.ocw（IP 與 2002 年 e2 相同）",
 "www_2002-01_home.png":"交大首頁：「網路大學 e.nctu」（2002-01）",
 "www_2005-02_campus-info.png":"交大校園資訊頁：「交大網路校園」（2005-02）",
 "www_2009-02_home.png":"交大首頁（2009-02）",
}
ERAS = [
 ("www","交大首頁怎麼連過去",lambda f:f.startswith("www_")),
 ("e","E.NCTU 交大網路校園（2000–2003）",lambda f:f.startswith("e_") or f.startswith("2003_e-nctu")),
 ("e2","E2 eCampus（2002–2007）",lambda f:f.startswith("e2_") or "e2_eCampus" in f or "E2_end" in f),
 ("e3","舊 E3 eCampus III（2006–2019）",lambda f:f.startswith("e3_") or "e3_NCTU_E3" in f or "copyright" in f),
 ("e3new","New E3（2017–2021）",lambda f:"e3new" in f or "NewE3" in f or "107-2" in f),
 ("nycu","e3.nycu（2021–2024）",lambda f:f.startswith("e3nycu") or "e3nycu" in f or "workshop" in f.lower()),
 ("e3p","e3p / E3@NYCU（2024–）",lambda f:f.startswith("e3p_") or "e3p_login" in f),
 ("live","2026-10 現況實測",lambda f:f.startswith("live_")),
]
files = sorted(f for f in os.listdir(os.path.join(root,"images")) if f.lower().endswith((".png",".jpg",".gif")))
used=set(); sections=[]
for key,title,pred in ERAS:
    fs=[f for f in files if f not in used and pred(f)]
    used.update(fs)
    if fs: sections.append((key,title,fs))
rest=[f for f in files if f not in used]
if rest: sections.append(("misc","其他",rest))
out=[]
for key,title,fs in sections:
    cards="".join(f'<figure class="{"logo" if f.endswith(".gif") or "logo" in f or "header" in f else ""}"><a href="images/{html.escape(f)}" target="_blank"><img loading="lazy" src="images/{html.escape(f)}" alt="{html.escape(C.get(f,f))}"></a><figcaption>{html.escape(C.get(f,f))}<code>{html.escape(f)}</code></figcaption></figure>' for f in fs)
    out.append(f'<section id="{key}"><h2>{html.escape(title)} <small>{len(fs)}</small></h2><div class="grid">{cards}</div></section>')
nav="".join(f'<a href="#{k}">{html.escape(t)}</a>' for k,t,_ in sections)
page=f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>E3 沿革圖庫</title><style>
:root{{--bg:#fafaf8;--fg:#1d1d1b;--muted:#6b6b66;--card:#fff;--line:#e3e2dc;--accent:#2457a6}}
@media (prefers-color-scheme:dark){{:root{{--bg:#161615;--fg:#ecebe6;--muted:#a09f99;--card:#20201e;--line:#34332f;--accent:#8fb3ff}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 -apple-system,BlinkMacSystemFont,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}}
header{{padding:28px 16px 8px;max-width:1200px;margin:auto}}h1{{margin:0 0 4px;font-size:24px}}header p{{margin:0;color:var(--muted)}}
nav{{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:14px;overflow-x:auto;white-space:nowrap;z-index:1}}
nav a{{color:var(--accent);text-decoration:none;font-size:14px}}main{{max-width:1200px;margin:auto;padding:0 16px 48px}}
h2{{font-size:18px;margin:32px 0 12px}}h2 small{{color:var(--muted);font-weight:normal;font-size:13px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}}
figure{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden}}
figure img{{display:block;width:100%;height:190px;object-fit:cover;object-position:top;background:#fff}}
figure.logo img{{object-fit:contain;padding:16px}}
figcaption{{padding:8px 10px;font-size:13px}}figcaption code{{display:block;color:var(--muted);font-size:11px;margin-top:2px;word-break:break-all}}
</style></head><body><header><h1>交大／陽明交大 E3 沿革圖庫</h1><p>點圖可開原圖。說明與出處見 README.md 與 notes/。</p></header><nav>{nav}</nav><main>{''.join(out)}</main></body></html>"""
open(os.path.join(root,"gallery.html"),"w").write(page)
print(len(files),"images;",[(k,len(fs)) for k,_,fs in sections])
