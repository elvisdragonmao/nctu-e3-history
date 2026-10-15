#!/usr/bin/env python3
"""Build e3-history.html: a self-contained page (all images inlined as base64).
Usage: make_site.py <project_root> <resized_jpg_dir>"""
import base64, json, os, sys, html

ROOT, IMGDIR = sys.argv[1], sys.argv[2]
ORIG = os.path.join(ROOT, "images")

def b64(path, mime):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

def shot(name):
    return b64(os.path.join(IMGDIR, name + ".jpg"), "image/jpeg")

WB = "https://web.archive.org/web/"

# ---------------------------------------------------------------- generations
GENS = [
 {"id": "e", "name": "E.NCTU 交大網路校園", "short": "E.NCTU", "host": "e.nctu.edu.tw",
  "period": "2000-11 → 約 2003", "family": "self",
  "who": "理學院「網路學習研究中心」自行開發；教務處網路教務組推廣",
  "tech": "FreeBSD + PostgreSQL + PHP；Phorum 3.2.11 討論區；用戶端 IE 4.0 以上",
  "logo": ("e_2001-03_profile_image001.png", "image/png"),
  "facts": [
   "2000-06 成立「網路大學推動小組」（魏哲和副校長召集）",
   "2000-10-17 第一次網路教材設計實務研習會：「已開發完成一套網路教學平台 E.NCTU」",
   "2000-11-04「交大網路校園 V1.0」全面開放測試",
   "功能分「個人工作室」與「組織建館」：教材管理、作業繳交與給分、討論區、行事曆、公告欄",
   "2002-10 有人上傳 mp3 遭 IFPI 通知，個人資料夾功能移除",
   "2003-02-25 最後一則公告；2006-05 起網域轉給 E3 使用",
  ],
  "paths": ["/index_new.htm（2000）", "/index_new.php（2001-06 起）", "/news/Profile.htm（關於本站）", "/bbs/（Phorum）"],
  "shots": [
   ("www_2002-01_home", "2002-01", "交大首頁「資訊捷徑」裡的「網路大學 e.nctu」", WB + "20020126120653/http://www.nctu.edu.tw/"),
   ("e_2000-12_home", "2000-12", "V1.0 時期首頁（切圖大多沒被存檔）", WB + "20001206215100/http://e.nctu.edu.tw/index_new.htm"),
   ("e_2001-06_home", "2001-06", "2001 改版首頁與「E.NCTU 人氣排行榜」", WB + "20010619061708/http://e.nctu.edu.tw/index_new.php"),
   ("e_2001-03_profile_architecture", "2001-03", "系統架構圖：IE 4.0 ↔ FreeBSD + PHP ↔ PostgreSQL", WB + "20010302091059im_/http://e.nctu.edu.tw/news/Profile.files/image010.jpg"),
   ("e_2002-02_home", "2002-02", "2002 年版首頁（中間 Flash 沒被存檔）", WB + "20020211224220/http://e.nctu.edu.tw/index_new.php"),
   ("e_2003-12_home", "2003-12", "最後版本首頁，只剩兩則公告", WB + "20031203233453/http://e.nctu.edu.tw/index_new.php"),
   ("e_2003-12_profile", "2003-12", "關於本站 Profile.htm（全頁）", WB + "20031204104846/http://e.nctu.edu.tw/news/Profile.htm"),
   ("e_2004-02_sitemap", "2004-02", "網站導覽：個人工作室／組織建館功能表", WB + "20040212011833/http://e.nctu.edu.tw/property/service/system/map.php"),
   ("www_2005-02_campus-info", "2005-02", "交大「校園資訊」頁仍連到「交大網路校園」", WB + "20050208093948/http://www.nctu.edu.tw/campus/index.html"),
  ]},
 {"id": "e2", "name": "E2 eCampus", "short": "E2", "host": "e2.nctu.edu.tw",
  "period": "2002-09 → 2007-09", "family": "ecampus",
  "who": "網路教務組 → 數位內容製作中心（DCPC）；廠商推測為三趨科技五校 e-Campus",
  "tech": "ASP.NET（C#、Visual Studio 7.0）；限 IE 6；ActiveX 上傳元件 GxWebFtp",
  "logo": ("e2_2002-10_logo.gif", "image/gif"),
  "facts": [
   "2002-09-14 最早一則最新消息；帳號沿用選課系統",
   "版本號 2.0.0.312（2003-06）→ 2.2.0.0613（2003-08）→ 4.0.2005.0217（2006–2009）",
   "同一主機另掛「台灣聯合大學網路教學課程選課登錄系統」",
   "2007-08-16 DCPC 公告：「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」",
   "2002 年的 IP 140.113.8.88，現在是 video.ocw.nycu.edu.tw",
  ],
  "paths": ["140.113.8.88/eCampus/default.aspx（2002）", "/eCampus/default.aspx", "/ECAMPUS_HELP/（說明）", "/Course/course.asp（四校選課）"],
  "shots": [
   ("e2_2002-10_login", "2002-10", "最早的登入頁，要先選身份（本機重建）", WB + "20021010082927id_/http://e2.nctu.edu.tw/eCampus/default.aspx"),
   ("e2_2003-01_login", "2003-01", "登入頁：ecampus logo 與交大校徽", WB + "20030109212507/http://e2.nctu.edu.tw/eCampus/"),
   ("e2_2004-09_course-signup", "2004-09", "台灣聯合大學網路教學課程選課登錄系統", WB + "20040907042736/http://e2.nctu.edu.tw/Course/course.asp"),
   ("e2_2006-04_login", "2006-04", "4.0.2005.0217 版登入頁（本機重建）", WB + "20060423035328id_/http://e2.nctu.edu.tw/ecampus/default.aspx"),
   ("e2_2007-08_dcpc_e2-end-notice", "2007-08", "DCPC 公告：E2 服務到九月底，請轉用 E3", WB + "20070917181422/http://dcpc.nctu.edu.tw/popup.aspx?type=1&id=3e3137da-d804-4c49-a4aa-4ebde347c987"),
  ]},
 {"id": "e3", "name": "舊 E3：eCampus III", "short": "舊 E3", "host": "e3.nctu.edu.tw",
  "period": "2006-02 → 2019-09", "family": "ecampus",
  "who": "教務處數位內容製作中心（DCPC）；底層與三趨科技 eCampus 3.0 的關係見「疑點」",
  "tech": "ASP.NET + Anthem.NET；IIS 6.0 → 8.5；frameset、整頁切圖；只支援 IE",
  "logo": ("e3_2006_copyright.gif", "image/gif"),
  "facts": [
   "「E3」= eCampus III／e-Campus 3.0；2006-07 起頁面標題固定為 eCampus III v…",
   "2006-03-08、03-15 在計網中心電腦教室辦說明會（校史館）",
   "2008-09 起 e3.nctu.edu.tw 根目錄轉到 DCPC 首頁，登入框放在那裡",
   "2010-09-16「好康訊息！新e3上線」；2014-06-27「舊版 e3 將於9月1日停止服務」",
   "每學期約 1,100 門課使用",
   "2017-09-27 公布 New E3 網址；「e3已於107下學期改版」（2019-02）",
  ],
  "paths": ["/NCTU_E3/lms2/（2006–2009）", "/NCTU_E3P/LMS2/（2009–2011）", "/NCTU_EASY_E3P/LMS2/（2010–2016）", "/NCTU_EASY_E3P/LMS3/（2016–2019）", "/NCTU_EASY_E3P/LMS31/（2018–2019）", "/mService/service.asmx（行動 API）"],
  "shots": [
   ("e3_2006-04_login", "2006-04", "首版登入頁：「國立交通大學網路教學平台 v.3」", WB + "20060421232920/http://e3.nctu.edu.tw/NCTU_E3/lms2/login.aspx"),
   ("e3_2007-09_dcpc_portal_home", "2007-09", "DCPC 首頁兼 E3 入口：E2 停用、e-Campus 3.0 教育訓練公告", WB + "20070911051426/http://dcpc.nctu.edu.tw/"),
   ("e3_2012-01_dcpc_portal_home", "2012-01", "2010 年改版後的 DCPC 首頁，藍色 e-Campus 登入框", WB + "20120101040640/http://dcpc.nctu.edu.tw/"),
   ("e3_2012-06_login_EASY_E3P", "2012-06", "NCTU_EASY_E3P 時期的登入頁，版面和 2006 年幾乎相同", WB + "20120615122430/http://e3.nctu.edu.tw/NCTU_EASY_E3P/LMS2/login.aspx"),
   ("e3_2016-01_dcpc_portal_home", "2016-01", "2016 年的 DCPC 首頁", WB + "20160116021718/http://dcpc.nctu.edu.tw/"),
   ("e3_2018-01_dcpc_portal_home", "2018-01", "新舊並行期：「New E3網址 http://e3.nctu.edu.tw/new」", WB + "20180113203023/https://dcpc.nctu.edu.tw/"),
  ]},
 {"id": "e3new", "name": "New E3", "short": "New E3", "host": "e3new.nctu.edu.tw",
  "period": "2017-09 → 2021-01", "family": "moodle",
  "who": "DCPC：「以moodle為基礎原型…為校內師生客製化」",
  "tech": "Moodle 3.3–3.7（推測）；自製佈景 theme_dcpc；Google OAuth2 外掛",
  "logo": ("logo_e3new_NewE3Cloud_orange_w.png", "image/png"),
  "facts": [
   "2017/09 版介紹手冊：有「匯入 E3 資源」，可把舊 E3 教材搬過來",
   "頁尾「Copyright ©2018 國立交通大學 數位內容製作中心」",
   "2019-02（107 下）全面改用；2020-07-28「新版e3」改版、換新 logo",
   "2020-02-17 陽明大學也引進 New E3（newe3.ym.edu.tw）",
   "2021-01-28 顯示維護頁，隔天搬到 e3.nycu.edu.tw",
  ],
  "paths": ["e3.nctu.edu.tw/new → e3new.nctu.edu.tw（2017）", "/login/index.php", "/theme/dcpc/news/（DCPC 公告系統）", "2021-05 起 301 → e3.nycu.edu.tw"],
  "shots": [
   ("2017-09_NewE3_intro_p1", "2017-09", "《New E3 數位教學平台介紹》2017/09 版", "https://e3.nycu.edu.tw/theme/dcpc/doc/OperationInstruction/"),
   ("wayback_2020-07-16_dcpc_e3_revised_107-2_notice", "2020-07", "DCPC 首頁：「e3已於107下學期改版」", WB + "20200716131006/http://dcpc.nctu.edu.tw/"),
   ("e3new_2020-11_login", "2020-11", "New e3 登入頁：「國立交通大學 數位教學平台」雲朵 logo", WB + "20201124064122/https://e3new.nctu.edu.tw/login/index.php"),
   ("2021-01-28_e3new_maintain", "2021-01-28", "維護頁：「本系統，進行系統維護中 暫停服務」", WB + "20210128080940/https://e3new.nctu.edu.tw/"),
  ]},
 {"id": "nycu", "name": "E3（合校後）", "short": "e3.nycu", "host": "e3.nycu.edu.tw",
  "period": "2021-01 → 2024-02（伺服器仍在線）", "family": "moodle",
  "who": "教務處教學資源組 → 數位教學中心",
  "tech": "同一套 Moodle 改網域；2021–22 年間升到 3.8–3.10（推測）；佈景仍是 dcpc",
  "logo": None,
  "facts": [
   "佈景版本日期 2021-01-29，比 2021-02-01 合校早三天",
   "頁尾改為「國立陽明交通大學 教學資源組」",
   "2022 起登入頁只給校外使用者，加上 Google Authenticator 二階段驗證",
   "2024-02-26 起登入頁 0 秒轉到 e3p",
   "2026-10 實測：Moodle 仍在運作；憑證 2026-10-20 到期",
  ],
  "paths": ["/login/index.php", "portal.nycu.edu.tw/portal/newe3（單一入口代號）", "meta refresh → e3p.nycu.edu.tw（2024-02 起）"],
  "shots": [
   ("wayback_2021-01-30_e3nycu_login", "2021-01-30", "合校前兩天上線的 e3.nycu", WB + "20210130053020/https://e3.nycu.edu.tw/login/index.php"),
   ("e3nycu_2022-12_login", "2022-12", "校外專用登入＋Google Authenticator", WB + "20221222071107/https://e3.nycu.edu.tw/login/index.php"),
   ("2023-09_E3workshop112-1_p7_old_platforms", "2023-09", "112-1 工作坊：陽明舊平台 eCampus／eeClass／NewE3(ym) 的處置", "https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1161839994642370560&type=s"),
   ("live_e3.nycu.edu.tw_2026-10", "2026-10-16", "現況：擋下轉址後看到的登入頁原貌", "https://e3.nycu.edu.tw/login/index.php"),
  ]},
 {"id": "e3p", "name": "E3@NYCU（e3p）", "short": "e3p", "host": "e3p.nycu.edu.tw",
  "period": "2024-02 → 今", "family": "moodle",
  "who": "教務處數位教學中心",
  "tech": "另建的 Moodle：4.0 → 4.1–4.3 → ≥4.5（推測）；Boost Union 佈景",
  "logo": None,
  "facts": [
   "112 學年第 2 學期（2024-02）啟用；jsrev 2024-02-23",
   "2024-03-28/29「112學年度第2學期 E3 新版期中工作坊」",
   "2024-05-02 影片「從舊E3到新E3一次搬移整門課程」：備份→還原（合併）",
   "校外帳號改用 Email 6 位數驗證碼",
   "「p」的意思沒有官方說明；舊 E3 從 2009 年起路徑就叫 NCTU_E3P",
  ],
  "paths": ["/login/index.php", "portal.nycu.edu.tw/portal/newe3p（單一入口代號）"],
  "shots": [
   ("e3p_2024-04_login", "2024-04", "最早的存檔：網站簡稱「E3@NYCU」", WB + "20240414071219/https://e3p.nycu.edu.tw/login/index.php"),
   ("e3p_2025-02_login", "2025-02", "Moodle 4.1–4.3 時期", WB + "20250212042345/https://e3p.nycu.edu.tw/login/index.php"),
   ("live_e3p.nycu.edu.tw_2026-10", "2026-10-16", "現況", "https://e3p.nycu.edu.tw/"),
  ]},
]

for g in GENS:
    g["shots"] = [{"img": shot(n), "date": d, "cap": c, "src": s} for n, d, c, s in g["shots"]]
    if g["logo"]:
        g["logo"] = b64(os.path.join(ORIG, g["logo"][0]), g["logo"][1])

# ---------------------------------------------------------------- gantt rows
# dates as "YYYY-MM-DD"; tail = period the server/archive stayed up after it stopped being the main platform
ROWS = [
 {"grp": "交大 → 陽明交大", "gen": "e",     "label": "E.NCTU", "host": "e.nctu.edu.tw", "fam": "self",    "s": "2000-11-04", "e": "2003-02-25", "tail": "2004-02-12", "tailNote": "最後一批內容存檔"},
 {"grp": "交大 → 陽明交大", "gen": "e2",    "label": "E2 eCampus", "host": "e2.nctu.edu.tw", "fam": "ecampus", "s": "2002-09-14", "e": "2007-09-30", "tail": "2009-07-29", "tailNote": "登入頁與說明頁仍有存檔"},
 {"grp": "交大 → 陽明交大", "gen": "e3",    "label": "舊 E3", "host": "e3.nctu.edu.tw", "fam": "ecampus", "s": "2006-02-24", "e": "2019-09-14", "tail": None},
 {"grp": "交大 → 陽明交大", "gen": "e3new", "label": "New E3", "host": "e3new.nctu.edu.tw", "fam": "moodle", "s": "2017-09-27", "e": "2021-01-28", "tail": None},
 {"grp": "交大 → 陽明交大", "gen": "nycu",  "label": "e3.nycu", "host": "e3.nycu.edu.tw", "fam": "moodle", "s": "2021-01-29", "e": "2024-02-26", "tail": "2026-10-16", "tailNote": "伺服器仍在線，但會轉到 e3p"},
 {"grp": "交大 → 陽明交大", "gen": "e3p",   "label": "e3p", "host": "e3p.nycu.edu.tw", "fam": "moodle", "s": "2024-02-23", "e": "2026-10-16", "tail": None},
 {"grp": "陽明大學（合校前）", "gen": None, "label": "陽明 eCampus III", "host": "e3.ym.edu.tw", "fam": "ecampus", "s": "2006-10-26", "e": "2018-11-01", "tail": None},
 {"grp": "陽明大學（合校前）", "gen": None, "label": "ee-class", "host": "eeclass.ym.edu.tw", "fam": "other", "s": "2015-05-15", "e": "2020-02-17", "tail": None},
 {"grp": "陽明大學（合校前）", "gen": None, "label": "New E3 (ym)", "host": "newe3.ym.edu.tw", "fam": "moodle", "s": "2020-02-17", "e": "2021-02-01", "tail": None},
]
EVENTS = [
 {"d": "2006-06-01", "t": "DCPC 成立"},
 {"d": "2019-02-15", "t": "107 下全面改用 New E3"},
 {"d": "2021-02-01", "t": "陽明交大合校"},
]

# ---------------------------------------------------------------- eCampus III builds (Wayback timestamp, <title>)
BUILDS_RAW = """20060227 NCTU E3 (v1.2006.0224.30796)
20060303 NCTU E3 (v1.2006.0302.36548)
20060410 NCTU E3 (v1.2006.0331.38355)
20060412 NCTU E3 (v1.2006.0411.37944)
20060421 NCTU E3 (v1.2006.0418.39906)
20060530 NCTU E3 (v1.1.60522.33125)
20060703 eCampus III v1.1.60629.38870
20060705 eCampus III v1.1.60704.40058
20060708 eCampus III v1.1.60707.43164
20060716 eCampus III v1.1.60712.04005
20060718 eCampus III v1.1.60717.37025
20060905 eCampus III v1.1.60831.41158
20061109 eCampus III v1.2.61103.00219
20061205 eCampus III v1.2.61130.38886
20070102 eCampus III v1.2.61228.37155
20070123 eCampus III v1.3.01237.21961
20070215 eCampus III v1.3.02147.01803
20070301 eCampus III v1.3.02187.27727
20070309 eCampus III v1.3.02187.29437
20070320 eCampus III v1.3.03167.32636
20070703 eCampus III v1.3.06287.38609
20070717 eCampus III v1.3.06287.05489
20070930 eCampus III v1.4.09217.23891
20071006 eCampus III v1.4.10057.36779
20071021 eCampus III v1.4.10157.17188
20071115 eCampus III v1.4.11147.21208
20071209 eCampus III v1.4.11237.17391
20080127 eCampus III v1.4.01228.16434
20080606 eCampus III v1.4.04078.24142
20080611 eCampus III v1.4.06058.17679
20080819 eCampus III v1.4.08138.17587
20080905 eCampus III v1.4.09048.31205
20080922 eCampus III v1.4.09198.33432
20081014 eCampus III v1.4.09308.26314
20081017 eCampus III v1.4.10168.21499
20081106 eCampus III v1.4.10298.26781
20081204 eCampus III v1.4.11258.20860
20081210 eCampus III v1.4.12098.37744
20090118 eCampus III v1.4.01139.29565
20090216 eCampus III v1.5.02169.01430
20090220 eCampus III v1.5.02199.01000
20090225 eCampus III v1.5.02249.01800
20090314 eCampus III v1.5.03129.01300
20090318 eCampus III v1.5.03169.00900
20090427 eCampus III v1.5.04279.01520
20090626 eCampus III v1.5.06269.01100
20090717 eCampus III v1.5.07039.01300
20091031 eCampus III v1.5.09309.01100
20100311 eCampus III v1.5.02250.01830
20100422 eCampus III v1.5.04120.01500
20100922 eCampus III v1.5.09130.01330
20110702 eCampus III v1.5.06011.01330
20110925 eCampus III v1.5.08241.01330
20111023 eCampus III v1.5.09271.01330
20111106 eCampus III v1.5.10281.00950
20120417 eCampus III v1.5.03262.00936
20120623 eCampus III v1.5.03272.01034
20121104 eCampus III v1.5.09212.01422
20130527 eCampus III v1.5.04103.01000
20140226 eCampus III v1.5.02193.01450"""
BUILDS = []
for line in BUILDS_RAW.splitlines():
    ts, title = line.split(" ", 1)
    v = title.split("v", 1)[1].rstrip(")")
    minor = "1.0" if v.startswith("1.2006") else v[:3]
    BUILDS.append({"d": f"{ts[:4]}-{ts[4:6]}-{ts[6:]}", "title": title, "minor": minor})
PATHS = [
 {"d": "2006-02-24", "t": "/NCTU_E3/lms2"},
 {"d": "2009-02-16", "t": "/NCTU_E3P"},
 {"d": "2010-09-13", "t": "/NCTU_EASY_E3P"},
 {"d": "2016-09-15", "t": "/LMS3"},
 {"d": "2018-06-01", "t": "/LMS31"},
]

# ---------------------------------------------------------------- Moodle versions (all inferred from M.cfg keys + YUI)
MOODLE = [
 {"host": "e3new.nctu.edu.tw", "segs": [{"s": "2017-09-27", "e": "2021-01-28", "v": "3.3–3.7", "lvl": 0}]},
 {"host": "e3.nycu.edu.tw", "segs": [{"s": "2021-01-29", "e": "2021-11-10", "v": "3.3–3.7", "lvl": 0, "note": "2021-08 ~ 2022-02 之間升級"},
                                     {"s": "2021-11-10", "e": "2026-10-16", "v": "3.8–3.10", "lvl": 1, "note": "2024-02 起只剩轉址"}]},
 {"host": "e3p.nycu.edu.tw", "segs": [{"s": "2024-02-23", "e": "2024-06-24", "v": "4.0", "lvl": 2},
                                      {"s": "2024-06-24", "e": "2025-07-01", "v": "4.1–4.3", "lvl": 3, "note": "2025-03 ~ 2025-11 之間升級"},
                                      {"s": "2025-07-01", "e": "2026-10-16", "v": "≥ 4.5", "lvl": 4}]},
]

DATA = {"gens": GENS, "rows": ROWS, "events": EVENTS, "builds": BUILDS, "paths": PATHS, "moodle": MOODLE}

tpl = open(os.path.join(os.path.dirname(__file__), "site_template.html"), encoding="utf-8").read()
out = tpl.replace("/*__DATA__*/null", json.dumps(DATA, ensure_ascii=False))
dst = os.path.join(ROOT, "e3-history.html")
open(dst, "w", encoding="utf-8").write(out)
print(dst, round(os.path.getsize(dst) / 1e6, 2), "MB")
