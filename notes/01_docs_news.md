# 01 文件／新聞／一手來源筆記：交大／陽明交大 E3 數位教學平台沿革

- 整理日期：2026-10-16
- 範圍：文字資料與一手來源（校史館、教務處／數位內容製作中心網站、Wayback 存檔頁面原文、廠商沿革、手冊 PDF、YouTube、GitHub、Dcard）
- 可信度標記：
  - **一手**：當時的官方頁面或存檔原文、官方手冊、系統本身回傳的字串（如 `<title>`、版權列）
  - **二手**：搜尋引擎摘要、論壇貼文、第三方專案、事後整理
  - **推測**：由 URL 結構、時間戳、版本字串推論，沒有明文佐證
- Wayback 連結格式：`https://web.archive.org/web/<時間戳>/<原網址>`。本筆記的原文都是用 `id_` 模式抓原始 HTML 後擷取的。

---

## 0. 最重要的發現（摘要）

1. **「E3」是「eCampus III／e-Campus 3.0」的簡稱**，不是「e-learning 第三代」之類的泛稱。2009 年 `e3.nctu.edu.tw/NCTU_E3P/lms2/` 的頁面標題是 `eCampus III v1.5.05209.01630`（一手）。校史館 2006 年條目寫「e-Campus 3.0（e3）上線」（一手）。2006 年登入頁的橫幅寫「國立交通大學網路教學平台 v.3 / e-campus」（一手，截圖已存）。
2. **舊 E3（2006–2019）的底層產品是三趨科技（3Probe Technologies）的 eCampus。** 三趨官網沿革寫：2002 年「交通大學、陽明大學、玄奘大學、中華大學與明新技術學院 e-Campus 五校聯合網路學習平台系統上線」，2006 年「eCampus Version 3.0 (E3) 非同步網路學習平台上〔線〕」以及「陽明大學eCampus建置上線」（一手，廠商自述）。陽明 `e3.ym.edu.tw` 的 eCampus 登入頁寫 `Copyright (R) 2006 3Probe`（一手）。交大的 E3 登入頁則印「版權所有 國立交通大學 Copyright © 2006」，由教務處數位內容製作中心維運與客製（一手）。
3. **系譜（交大端）**：E.NCTU（2000，理學院網路學習研究中心自製，FreeBSD+PostgreSQL+PHP）→ E2／eCampus（2002-09，ASP.NET，五校聯合平台）→ E3／eCampus III（2006-02/03 上線，ASP.NET，IE only）→ New E3（e3new，Moodle 客製，106 學年 2017-09 起；107 下 2019-02 全面改版）→ e3.nycu.edu.tw（2021-01 底合校時改網域，Moodle）→ 新版 E3（e3p.nycu.edu.tw，112 學年第 2 學期 2024-02 起，Moodle + boost_union 佈景）。
4. **關鍵日期**
   - 2000-10-17：E.NCTU 第一次網路教材設計研習會，「已開發完成…即將開放全校師生使用」（一手）
   - 2002-09-14／09-23：e2 eCampus 最早公告，「本校師生請使用選課系統帳號/密碼登入本系統」（一手）
   - 2006-03：e-Campus 3.0（e3）上線，3/8、3/15 在計網中心電腦教室二辦說明會（校史館，一手）。Wayback 最早頁面為 2006-02-27，版本字串是 `NCTU E3 (v1.2006.0224.30796)`
   - 2007-08-16：「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」（數位內容製作中心公告，一手）
   - 2017-09：New E3 介紹手冊「2017/09 版」，寫明「以moodle 為基礎原型，由交通大學數位內容製作中心為校內師生客製化」（一手）
   - 107 學年下學期（2019-02）：「e3已於107下學期改版 請按此進入New e3使用」（dcpc.nctu.edu.tw 首頁，一手）
   - 2020-02-17：陽明大學引進交大 New E3（newe3.ym.edu.tw），eeClass 自 1082 起停止新開課（陽明教學資源組公告標題，二手搜尋摘要；陽明在校學生頁連結為一手）
   - 2021-01-28：e3new 顯示「本系統，進行系統維護中」（一手，圖已存）；2021-01-30 `e3.nycu.edu.tw` 首次被存檔，版權是「國立陽明交通大學 教學資源組」（一手）；2021-02-01 合校
   - 2024-02（112-2）：新版 E3（e3p）啟用。2024-03-28／29 辦「112學年度第2學期E3新版期中工作坊」，2024-05-02 發布「從舊E3到新E3一次搬移整門課程」影片（一手，YouTube 官方承辦人頻道）
5. **找不到的部分**：官方「E3+」命名或「e3p 的 p 代表什麼」的說明；舊 E3（ASP.NET）正式關站公告；以 E3 為研究對象的學位論文（機構典藏 API 檢索沒有命中）。

---

## 1. 時間軸總表

| 時間 | 事件 | 系統／網址 | 開發／維運 | 技術 | 可信度 | 主要來源 |
|---|---|---|---|---|---|---|
| 2000-06 | 網路大學推動小組成立（召集人魏哲和副校長，執行秘書陳明璋） | — | 校方 | — | 一手 | 校史館 1991-2000 [S1]；E.NCTU Profile [S2] |
| 2000-07 起 | E.NCTU 系統開始開發 | e.nctu.edu.tw | 理學院「網路學習研究中心」（林松山院長） | FreeBSD + PostgreSQL + PHP | 一手 | [S2] |
| 2000-10-17 | 第一次網路教材設計實務研習會：「已開發完成一套網路教學平台 E.NCTU，即將開放全校師生使用」 | e.nctu.edu.tw | 網路教務組、網路學習研究中心 | — | 一手 | [S3] |
| 2000-11-01 | 教務處「網路教務組」設立（89 學年第一次臨時校務會議通過） | — | 教務處 | — | 一手 | [S1] |
| 89 學年上學期（2000 秋） | 「交大網路校園」（E.NCTU）正式啟用 | e.nctu.edu.tw | 同上 | V2.0 加入繳交作業、管理統計 | 一手 | [S1][S2] |
| 2000-12-06 | e.nctu.edu.tw 最早 Wayback 存檔 | — | — | — | 一手 | CDX |
| 2002-09 | e2 eCampus 上線（最早公告 2002/09/14） | e2.nctu.edu.tw/eCampus/ | 三趨科技 e-Campus 五校聯合平台（推測即此系統） | ASP.NET（.aspx） | 一手（存檔）＋推測（廠商對應） | [S4][S5] |
| 2003-02 | E.NCTU 最後一則站內公告（2003-02-25） | e.nctu.edu.tw/Board/news | — | — | 一手 | [S6] |
| 2005–2006 | 網路教務組（與出版組）改組為「數位內容製作中心」 | — | 教務處 | — | 一手（年份兩說：校史館列在 2005/2006 交界，中心自述「民國95年」） | [S7][S8] |
| 2006-02-27 | 最早的 E3 頁面：`NCTU E3 (v1.2006.0224.30796)` | e3.nctu.edu.tw/NCTU_E3/lms2/ | 數位內容製作中心（版權列：國立交通大學） | ASP.NET、frameset、ActiveX XMLHTTP；只支援 IE | 一手 | CDX＋存檔原文 |
| 2006-03 | 「e-Campus 3.0（e3）上線」，3/8、3/15 在光復校區計網中心電腦教室二辦說明會 | 同上 | 同上 | — | 一手 | 校史館 2001-2010 [S7] |
| 2006 | 三趨科技：「eCampus Version 3.0 (E3) 非同步網路學習平台上〔線〕」「陽明大學eCampus建置上線」 | — | 三趨科技 3Probe | — | 一手（廠商自述） | [S5] |
| 2006-10 | 陽明 e3.ym.edu.tw 上線，標題 `eCampus III v1.1.60807.37920`，登入頁版權圖仍是「國立交通大學」 | e3.ym.edu.tw/E3/LMS2/ | 陽明（三趨建置） | 同一套 | 一手 | CDX＋存檔 |
| 2007-08-16 | 「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」 | — | 數位內容製作中心 | — | 一手 | [S9] |
| 2007-09-07 | 「e3同步、e3同步上線了！」 | — | 同上 | — | 一手 | [S9] 截圖 |
| 2009-02 | E3 路徑出現 `NCTU_E3P/lms2`，標題 `eCampus III v1.5.05209.01630` | e3.nctu.edu.tw/NCTU_E3P/ | 同上 | — | 一手 | CDX＋存檔 |
| 2009–2021 | e3.nctu.edu.tw 根目錄 302 轉到 dcpc.nctu.edu.tw（中心首頁兼 E3 登入入口） | dcpc.nctu.edu.tw | 同上 | — | 一手 | Wayback 302 標頭 |
| 2010-09 | 路徑 `NCTU_EASY_E3P/LMS2` | — | — | — | 一手 | CDX |
| 2013 | 「iCT」行動學習 App，e-Campus 功能將移植過去 | — | 交大（「結合學生力量」） | iOS/Android | 一手 | [S10] |
| 2013–2016 | E3 行動 API `mService/service.asmx`（GetSystemNewsList 等） | e3.nctu.edu.tw/mService/ | — | ASMX Web Service | 一手（存檔）＋二手（GitHub 文件） | CDX；[S20] |
| 2016-03 | 路徑 `NCTU_EASY_E3P/LMS3` | — | — | — | 一手 | CDX |
| 2017-09 | New E3 介紹「2017/09 版」：Moodle 為原型，數位內容製作中心客製 | e3new.nctu.edu.tw | 數位內容製作中心 | Moodle 3.x（推測 ≤3.6，有 dock 模組） | 一手 | [S11] |
| 106 學年（2017-18） | 「自106學年起，交大的數位教學平台有了許多變革」「未來舊有的e3將不再升級」 | — | — | — | 二手（校園公告系統內文已不存在，只剩搜尋摘要與附件名「106下學期數位平台活動預告」） | [S12] |
| 2017-11-01 | e3new 最早 Wayback 存檔 | — | — | — | 一手 | CDX |
| 2018-05 | 舊 E3 路徑 `NCTU_EASY_E3P/LMS31`（最後一代 ASP.NET 版） | — | — | — | 一手 | CDX |
| 2019-02（107 下） | 「e3已於107下學期改版 請按此進入New e3使用」 | dcpc.nctu.edu.tw | 同上 | — | 一手 | [S13] |
| 2019-09 | 舊 E3（LMS31）最後一批正常存檔 | — | — | — | 一手 | CDX |
| 2020-02-17 | 陽明「New E3數位教學教學平台於109年2月17日正式上線」，「因應兩校合併，1082學期引進交大E3New 數位教學平台（原eeClass將於1082起停止提供開課服務）」 | newe3.ym.edu.tw | 陽明教學資源組 | Moodle（交大 New E3） | 二手（標題與摘要來自搜尋結果，原頁 DNS 已失效）＋一手（陽明在校學生頁連結） | [S14][S15] |
| 2020-07-28 | 「新版e3」：功能更多、使用更便利，請利用「進階設定」 | aadm.nctu.edu.tw/dcpc/?p=471 | 數位內容製作中心 | 新 logo `NewE3Cloud_orange_w.png`（上傳時間 2020-08-05） | 一手 | [S16] |
| 2020-10／2021-04 | 舊 E3 的 `NCTU_Easy_E3P/LMS2` 路徑在存檔中回 404 | — | — | — | 一手（只能證明最晚此時已下線） | CDX |
| 2021-01-28 | e3new 顯示「本系統，進行系統維護中 暫停服務」 | e3new.nctu.edu.tw | — | — | 一手 | 存檔圖 |
| 2021-01-30 | `e3.nycu.edu.tw` 首次被存檔，標題「e3 數位教學平台」，版權「©2021 國立陽明交通大學 教學資源組」 | e3.nycu.edu.tw | 教務處教學資源組（後稱數位教學中心） | Moodle，theme `dcpc` | 一手 | 存檔原文 |
| 2021-02-01 | 國立陽明交通大學成立 | — | — | — | 一手 | 校史館 2011-現今 [S17] |
| 2021-02-24 | 【E3 問答集】教師篇：登入舊版「New e3」只會看到 1091 課程，請由 NYCU 單一入口登入 | aa.nycu.edu.tw | 數位教學中心 | — | 一手 | [S18] |
| 2021-05 | e3new.nctu.edu.tw 301 轉到 e3.nycu.edu.tw | — | — | — | 一手 | Wayback 標頭 |
| 2022-06 | e3.nctu.edu.tw 根目錄 302 轉到 e3.nycu.edu.tw | — | — | — | 一手 | Wayback 標頭 |
| 2023-09 | 112-1 工作坊投影片：陽明舊平台 eCampus、eeClass 網站已關閉，資料需申請；NewE3(ym) 在 newe3.ym.edu.tw（合校前 E3 資料）；eCampus、eeClass 服務到 116.7.31（2027-07-31）止 | — | 數位教學中心 | — | 一手 | [S19] |
| 約 2024-01 | Dcard：「下學期的課程都會在New E3上」，「在網址e3後面多打一個p就是了」，入口網連結 `portal.nycu.edu.tw/portal/newe3p` | — | — | — | 二手 | [S21] |
| 2024-02（112-2） | 新版 E3（e3p）啟用。存檔頁 jsrev＝2024-02-23，themerev＝2024-03-07 | e3p.nycu.edu.tw | 數位教學中心 | Moodle，theme `boost_union`（另有 `dcpc2021.css`） | 一手（影片、存檔）＋推測（確切啟用日） | [S22] |
| 2024-03-28／29 | 「112學年度第 2學期E3新版期中工作坊」，陽明校區圖資大樓 401 | — | E3數位平台推廣小組 | — | 一手 | [S22] |
| 2024-04-14 | e3p 最早 Wayback 存檔，標題 `Log in to the site \| E3@NYCU` | — | — | — | 一手 | CDX |
| 2024-05-02 | 「從舊E3到新E3一次搬移整門課程」影片；後有同名問答（114-03-26） | — | 數位教學中心 | Moodle 備份／還原（合併） | 一手 | [S22][S23] |
| 2024-12-17 | 「E3網站使用協議」修訂，平台稱「E3數位學習平臺」 | — | 教務處 | — | 一手 | [S24] |
| 2026-10（現況） | e3p：Moodle，推測 ≥4.5（`mod/subsection` 存在、`mod/qbank` 不存在）；e3.nycu.edu.tw 仍在線，theme `dcpc`，推測 3.7–3.11 | — | — | — | 推測（路徑探測） | 本次探測 |

---

## 2. 各世代細節

### 2.1 E.NCTU「交大網路校園」（e.nctu.edu.tw，2000–約 2003）

- **定位與開發者**（一手，[S2] Profile.htm，2001-03 起有存檔，使用者提供的是 2003-12-04 版）：
  - 「E.NCTU(網址為e.nctu.edu.tw)是『網路學習研究中心』所建構的第二個網站。(第一個是數學學習館，網址為informath.nctu.edu.tw。)」
  - 「交通大學『網路大學推動小組』於民國89年6月成立，由魏副校長擔任召集人、陳明璋博士擔任執行秘書…在教務處成立『網路教務組』負責處理網路大學教務工作，理學院林院長領導的『網路學習研究中心』負責網路教學的系統平台之發展與應用」
  - 開發時程與人力：「自2000年07月至今」，從 3 名 Internet 軟體工程師擴編到「11人規模的專案型組織」。
  - 技術：「Server端均以Open Source Solution 之軟體為採用重點」，「FreeBSD (O.S.) ＋PostgreSQL（DataBase）＋PHP」。客戶端需求：Pentium、32M RAM、Windows 95 以上。
  - 功能：「個人工作室」與「組織建館」兩大部分；「在V2.0版時更有『繳交作業』及『管理統計』等功能」。
  - 聯絡：網路學習研究中心，理學院科學一館 307 室，help@E.NCTU.edu.tw。
  - 願景：「多校別集中管理」「各校分散發展應用」，成為學界 eLearning 通用平台提供者。
- **啟用**：
  - 校史館（1991-2000 頁，一手）：「網路大學推動小組於八十九學年度上學期推出全國最先進的網路大學『交大網路校園』（E.NCTU，網址：http://e.nctu.edu.tw）。」另有「『交大網路校園』（E‧NCTU）系統正式啟用。」網路教務組成立日為「2000年11月1日國立交通大學八十九學年度第一次臨時校務會通過」，並稱是「全國首創」。[S1]
  - 研習會公告（一手，[S3]）：八十九年十月十七日（2000-10-17）浩然圖書資訊中心地下室國際會議廳；主辦為教務處網路教務組、網路學習研究中心；主持人是蔡文祥教務長、林松山院長。
- **站內公告**（一手，[S6]，Big5 原文）：
  - 2001-04-29 停機進行資料庫系統升級
  - 2001-09-10「你可以自行設定是否開啟小精靈囉」
  - 2002-03-15 登入方式：帳號是學號或教職員代號，密碼預設身分證後六碼；問題洽「網路教務組(50151~3)」
  - 2002-10-15 因 IFPI 通知，要求刪除個人資料夾中的 mp3；2002-10-18 移除個人資料夾上傳功能
  - 2003-02-25 科管所推廣教育學分班登入方式（最後一則）
- **相關研究計畫**（一手書目）：曾憲雄，《網路教學系統平台與內容標準化規劃計畫》，國科會，2001。[S25]
- **下線**：沒有找到明確公告。Wayback 年度存檔量：2001 年 946 筆、2002 年 954 筆、2003 年 472 筆，2004 年起幾乎沒有（推測 2003 年後由 E2 取代）。

### 2.2 E2：eCampus（e2.nctu.edu.tw，2002-09 – 2007-09）

- **存檔原文**（一手，[S4]，2002-10-10）：頁面標題 `eCampus Login Page`；身分可選「系統管理員／教師／學生」；最新消息有「2002/09/14：新手請看下方之相關連結」「2002/09/23：本校師生請使用選課系統帳號/密碼登入本系統.」「2002/09/24：系統更新說明」；「火線討論區」最早貼文日期是 2002/10/08。
- **技術**：ASP.NET（`default.aspx`、`eCampus_GuestView/…aspx`），說明文件路徑是 `ECAMPUS_HELP`（一手，CDX）。
- **開發者**：三趨科技沿革寫 2002 年「交通大學、陽明大學、玄奘大學、中華大學與明新技術學院e-Campus五校聯合網路學習平台系統上線」（一手，[S5]）。e2 的產品名「eCampus」、上線年份都和這筆紀錄吻合，所以**推測 E2 就是這套五校聯合 e-Campus**。
- **E2 這個名稱**：沒有找到「E2＝eCampus II」的明文。但 E3 的正式名稱是「eCampus III／e-Campus 3.0」，所以「E2＝第二代 e-Campus」的推論很自然（推測）。
- **停止服務**：數位內容製作中心首頁 2007/08/16 公告「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」（一手，[S9]，截圖已存）。e2 主機到 2009 年仍有存檔，但那是 `fsreg`（報名）、`ust` 等其他系統。

### 2.3 E3：eCampus III／e-Campus 3.0（e3.nctu.edu.tw，2006 – 2019，「舊 E3」）

- **名稱證據（一手）**
  - 2006-02-27 起首頁標題：`NCTU E3 (v1.2006.0224.30796)`（路徑 `/NCTU_E3/lms2/Default.aspx`）
  - 2009-02-16 `/NCTU_E3P/lms2/` 標題：`eCampus III v1.5.05209.01630`
  - 2006 年登入頁圖像橫幅：「國立交通大學網路教學平台 v.3」＋「e-campus」字樣（截圖 `wayback_2006-07-03_e3_NCTU_E3_login.png`）
  - 校史館：「e-Campus 3.0（e3）上線。於3月8日、15日在在光復校區計網中心電腦教室二，舉辦使用說明講解。」（位於 2006 年段落，前後文是九十四學年度第三次校務會議）[S7]
  - 2007-09 數位內容製作中心公告：「9月6日 10:00~12:00【e-Campus 3.0 網路教學平台教育訓練課程】」[S9]
- **開發／維運**
  - 廠商：三趨科技 2006 年「eCampus Version 3.0 (E3) 非同步網路學習平台上〔線〕」（一手，[S5]）。陽明同一產品的登入頁寫「Copyright (R) 2006 3Probe. All rights reserved.」（一手，2015-01-20 存檔）。
  - 校內：交大登入頁版權圖是「版權所有 國立交通大學 Copyright © 2006 National Chiao Tung University」（一手，圖已存）。數位內容製作中心「成員執掌」（2007）列出曾文椿負責「網路教學平台系統維護與技術開發」，中心服務項目包括「網路教學平台的開發與維運」「平台內全校課程的建置、全校老師與學生的帳號建立」（一手，[S8]）。
  - 綜合判斷（推測）：三趨提供 eCampus 3.0 核心，交大掛校方版權並由數位內容製作中心長期客製與維運。陽明 2006–2007 年的 e3.ym.edu.tw 甚至沿用印有「國立交通大學」的版權圖，顯示兩校共用同一套佈署來源。
- **功能**（一手，dcpc「教學平台介紹」2007，[S8]）：可隨時切換繁中、英文、簡中三種語系；課程旁聽、訪客參觀；公式輸入工具與線上文章編輯；挑選歷年作業與討論供觀摩；詳盡的學習紀錄；評量、點名與缺席扣分；分組；數個課程樣版。
- **限制**：「本平台目前僅適用IE, 使用其它的Browser無法保証所有功能皆能正常執行」（2006-12 login_news，一手）。程式使用 `ActiveXObject("Microsoft.XMLHTTP")`。
- **規模**：「每學期約有1100門課程透過e-Campus輔助教學」（dcpc 教學平台介紹，2017–2021 存檔，一手，[S10]）
- **URL／版本演進**（一手，CDX 統計，括號是首次到末次存檔）
  - `/NCTU_E3/lms2/`（2006-02 → 2016-10）
  - `/NCTU_E3P/lms2/`（2009-02 → 2019-09）
  - `/NCTU_EASY_E3P/LMS2/`（2010-09 → 2018-07）
  - `/NCTU_EASY_E3P/LMS3/`（2016-03 → 2018-06）
  - `/NCTU_EASY_E3P/LMS31/`（2018-05 → 2019-09）
  - 其他：`/mService/service.asmx`（2016，行動 API）、`/CourseOutline/`（2008–09）、`/ust/`、`/preu/`（2007–08）、`/cgestu/`（2012）
  - 「E3P」「EASY_E3P」的含意沒有找到說明（推測是 E3 Plus／新版程式分支）。陽明端同期是 `ecampus3/learn`（2008-12 起）與 `ecampus3p/learn`（2010-03 起），「3P」與交大的「E3P」對應，推測都是 eCampus 3 Plus。
- **入口**：2006 年根目錄轉到 `NCTU_E3/lms2/Default.aspx`；2009–2021 年根目錄 302 轉到 `dcpc.nctu.edu.tw`，數位內容製作中心首頁左側就是 e-Campus 登入框（一手，Wayback 標頭與截圖）。
- **行動化**
  - 2013 年「交大結合學生力量首創第一個行動學習平台APP『iCT』」，「e-Campus的重要功能將移植到iCT上」（一手，[S10]）
  - 2017/10/11 dcpc 首頁有「iNCTU App 下架說明」（一手，標題）
  - GitHub `Spiderpowa/NCTU-E3MobileAPIDocument`（2013-09，「NCTU E3 System Mobile API Document」）、`Spiderpowa/NCTU-E3X`（2013，「A modern E3 System」）（二手）
  - Android App `Team214-tw/NCTUe4`（2018-03），可同時瀏覽「NCTU e3（dcpc.nctu.edu.tw/index.aspx）」與「NCTU New e3」（二手）
- **舊 E3 退場**
  - 106 學年起「未來舊有的e3將不再升級」（二手，[S12]）
  - 「e3已於107下學期改版 請按此進入New e3使用」（dcpc.nctu.edu.tw 首頁，2020-07-16、2021-01-11 存檔可見；2019-07-20 版尚無此字樣，一手，[S13]）
  - 舊 E3 頁面的正常存檔停在 2019-09-14；2020-10-25 `NCTU_Easy_E3P/LMS2/...` 回 404；2021-04-13 `NCTU_EASY_E3P/LMS2/tea_course_index.aspx` 回 404（一手）
  - 2021-04 根目錄仍轉 dcpc；2021-12 dcpc.nctu.edu.tw 已 404；2022-06 根目錄改轉 e3.nycu.edu.tw（一手）
  - 合校後 E3 手冊（2022-03、2023-04、2025-08 版）的系統選單仍有「e3 線上學習系統」，說明是「如要尋找舊課程請利用系統選單的歷年課程及 E3 線上學習系統（舊eCampus)進行查詢」，且課程工具有「匯入 E3 資源（可提供 eCampus 的教材轉入）」（一手，[S26]）。可見舊 eCampus 資料仍以某種形式保留可查。
  - **找不到**：舊 E3 正式關站日期的公告。

### 2.4 New E3（e3new.nctu.edu.tw，2017-09 – 2021-01）

- **一手定義**：「New E3 數位教學平台 是以moodle 為基礎原型，由交通大學數位內容製作中心為校內師生客製化而開發出來的網路學習平台。」「登入網址：http://e3new.nctu.edu.tw」。手冊標「2017/09 版」，PDF 建立時間是 2017-09-22，作者欄 `G0325`。功能包含「匯入E3 資源」：「系統會檢查登入的帳號在E3 的所有課程，使用者可選擇課程要匯入的教材、作業或公告等資源到對應的NewE3 單元」。[S11]（PDF 已存）
- **登入頁**（一手，2019-11-18 存檔）：標題 `New e3 數位教學平台: 登入本網站`；版權「Copyright ©2018 國立交通大學 數位內容製作中心 版權所有」；有圖形驗證碼（securimage）；有 Google OAuth2 外掛的 CSS（`auth/googleoauth2`）。
- **技術**：Moodle，theme `dcpc`。頁面載入 `moodle-core-dock` 模組（Moodle 3.7 起移除 dock），所以推測是 **Moodle 3.6 以下的 3.x**（推測）。themerev 1571287079 對應 2019-10-17。
- **時程**
  - 2017-09：手冊與上線（106 學年）
  - 2017-11-01：首次存檔（根目錄 302）
  - 2019-02（107 下）：全面改用 New E3（[S13]）
  - 2020-07-28：「新版e3」UI 改版公告（[S16]）；同期新 logo `NewE3Cloud_orange_w.png`（2020-08-05）
  - 2021-01-28：維護頁（`maintain.png`）
  - 2021-05 起 301 轉到 e3.nycu.edu.tw
- **New E3 也承載中心的新聞系統**：`https://e3new.nctu.edu.tw/theme/dcpc/news/news_view.php?d=…`（dcpc 首頁連結，一手）
- **社群工具**：`mlouielu/e3dump`（2019-05-21，「No worries about e3 shutdown」，程式目標為 `e3new.nctu.edu.tw/local/courseextension/…`，二手）。

### 2.5 合校後：e3.nycu.edu.tw（2021-01 – ，現仍在線）

- 2021-01-30 首次存檔：標題「e3 數位教學平台: 登入本網站」；版權「Copyright ©2021 國立陽明交通大學 教學資源組 版權所有」；「記住帳號 (提醒：本校人員請使用單一入口帳號密碼)」；theme `dcpc`，themerev 1611904248（2021-01-29）。程式結構與 e3new 相同，推測是同一套 Moodle 直接改網域與品牌（推測）。
- 【E3 問答集】教師篇（110-02-24，一手，[S18]）：從陽明交大入口網的「校務系統連結 → 陽明交通大學 → e3數位教學平臺」進入；「課程只顯示1091學期」是因為登入了舊版「New e3」；舊系統員編從 5 碼改成 6 碼造成部分帳號對應錯誤；課程大綱匯入功能移除，改與課務系統整合。
- 業務單位：2021 年版權列為「教學資源組」（交大校區在科學一館 1F）。現在教務處網站以「數位教學中心」名義發布 E3 資訊，業務包括「全校師生帳號建立、平臺開發與維運、平臺內全校課程的建置、舉辦數位教學工作坊…」（一手，[S27]）。
- 2021-03-18 起有「110.03.18 E3 工作坊(一)」等影片（一手，YouTube）。
- 現況（2026-10 本次探測）：login 頁仍是 theme `dcpc`，版權寫 2022，校外帳號要用 Google Authenticator 兩步驟驗證。沒有 `reportbuilder`（Moodle 4.0+），沒有 dock 模組，推測是 **Moodle 3.7–3.11**（推測）。

### 2.6 新版 E3：e3p.nycu.edu.tw（2024-02 – 今）

- **啟用時間**：112 學年第 2 學期（2024-02）。證據如下：
  - YouTube（數位教學中心承辦人頻道 @nycu_derek）：「1122 E3 新版教學工作坊(1)」上傳於 2024-03-28；「20240328.112學年度第 2學期E3新版期中工作坊[搶鮮版]」的說明寫「如果您錯過了期初工作坊，正傷腦筋不熟悉新E3功能…E3數位平台推廣小組再次為新的版本E3舉辦教育訓練…◆時間:113年3月28日…◆活動地點: 陽明校區圖資大樓401教室」（一手）
  - 「從舊E3到新E3一次搬移整門課程-(字幕)」上傳於 2024-05-02（一手）
  - 「如何從Moodle樣板切換回E3樣板」上傳於 2024-05-20：「新版的E3介面大更動…進入版面設定後可以看到【E3 Style】與【MoodleE3 Style】」（一手）
  - Dcard（約 2024-01，二手）：「有看到說下學期的課程都會在New E3上」，回覆提到「在網址e3後面多打一個p就是了」以及入口網 `newe3p` 連結
  - 存檔頁的 jsrev 1708689256（2024-02-23）、themerev 1709798439（2024-03-07）（一手，推論部署時間）
- **登入頁**（2024-04-14 存檔，一手）：標題 `Log in to the site | E3@NYCU`；「本登入頁僅供校外使用者 (含 學分班學生 、 校際選修) 進入；本校 師生 、 職員 ，請由 【 單一入口 】 進入」；Email 6 位數驗證碼；logo「國立陽明交通大學 數位教學平台」雲朵 e3 圖案（截圖已存）。
- **技術**：Moodle，theme `boost_union`（仍載入 `theme/boost_union/style/dcpc2021.css`）；有 `quiz/accessrule/proctoring` 外掛；2026 年探測到 `mod/subsection`（Moodle 4.5 新增），所以現在推測是 **Moodle 4.5.x**（推測）。
- **舊站→新站搬移**（一手，[S23]，114-03-26）：在舊站用課程備份產生備份檔（WebFetch 摘要寫副檔名 .mhz，Moodle 標準是 .mbz，未逐字核對），到新站「還原」並選「合併」而非取代；上傳與下載上限 2G。
- **名稱**
  - 官方文件稱「E3數位教學平臺」「E3數位學習平臺」（使用協議，113-12-17 修訂），頁首是「E3@NYCU」。**沒有找到「E3+」作為官方名稱的來源。**
  - 「e3p」的「p」：**找不到官方說明**。可以參考的脈絡（推測）：舊 E3 就有 `NCTU_E3P`、`NCTU_EASY_E3P` 路徑（2009–2019），陽明 eCampus 有 `ecampus3p`；入口網代號是 `newe3p`。「P」可能是沿用舊慣例的 Plus，但沒有證據。
- 2025-12-05 問答：「e3 登入驗證方式，增加"手機驗證方法"(僅限手動登入 e3p.nycu.edu.tw)」（一手，[S28]）。

---

## 3. 陽明大學端的數位學習平台（合校前）

| 平台 | 網址 | 期間 | 廠商／來源 | 證據 | 可信度 |
|---|---|---|---|---|---|
| e-Campus 五校聯合平台 | （未知） | 2002– | 三趨科技 | 三趨沿革 2002 | 一手（廠商） |
| eCampus III | e3.ym.edu.tw（`/E3/LMS2` 2006-10 → `/ecampus3/learn` 2008-12 → `/ecampus3p/learn` 2010-03、`/sso/learn` 2011-10），後移至 `portal.ym.edu.tw/eCampus3P/learn/` | 2006-10 → 約 2018（2018-04 仍 200，2018-11 起 302） | 三趨科技（「Copyright (R) 2006 3Probe」）；2006–07 登入頁版權圖卻是「國立交通大學」 | 標題 `eCampus III v1.1.60807.37920`（2006-10）、`eCampus III v1.5.01130.01630`（2010-03）；三趨沿革「陽明大學eCampus建置上線」（2006） | 一手 |
| ee-class 易課平台（「國立陽明大學 數位課程平台」） | eeclass.ym.edu.tw | 公告「歡迎使用 ee-class 易課平台」期間 2015-05-15 起；Wayback 2017-07 起；1082 起不再新開課 | FormosaSoft（「© Copyright since 2003 by FormosaSoft Corporation」） | 2017-11-01 存檔原文 | 一手 |
| New E3（交大 New E3） | newe3.ym.edu.tw | 2020-02-17 上線（1082） → 2021-02 合校 | 交大數位內容製作中心的 New E3（Moodle） | 陽明教學資源組公告標題「New E3數位教學教學平台於109年2月17日正式上線」與摘要「為因應兩校合併，1082學期引進交大E3New 數位教學平台（原eeClass將於1082起停止提供開課服務）」；陽明「在校學生」頁（2021-08 存檔）連結：「數位課程平台(New E3) → https://newe3.ym.edu.tw/」「數位課程平台(ee-class,1082起不提供新開課)」「非同步教學課程(Ecampus) → https://portal.ym.edu.tw/eCampus3P/learn/default.aspx」 | 二手（公告內文）＋一手（連結頁） |

- 合校後的處置（112-1 工作坊投影片，2023-09，一手，[S19]，截圖已存）：
  - 「eCampus 、eeClass :網站已關閉，需申請取得」
  - 「NewE3：https;//newe3.ym.edu.tw(合校前E3資料)」
  - 「eCampus 、eeClass服務期限：116.7.31止終止服務，若有特殊需求請洽教資組（陽明校區承辦人）」
- 三趨科技 2016 年另有「陽明大學學習諮詢系統上線」（一手，廠商）。

---

## 4. 單位沿革（與 E3 相關）

| 時間 | 單位 | 說明 | 來源 | 可信度 |
|---|---|---|---|---|
| 1998 起 | 理學院「網路學習研究中心」 | 林松山院長整合資源建構「網路高中數學學習館」後成立；負責 E.NCTU 平台開發 | [S2][S1] | 一手 |
| 2000-06 | 網路大學推動小組 | 魏哲和副校長召集 | [S1] | 一手 |
| 2000-11-01 | 教務處「網路教務組」 | 全國首創；網路大學教務 | [S1] | 一手 |
| 民國95年（2006）；校史館列在 2005–2006 | 教務處「數位內容製作中心」(NCTU Center for Digital Content Production, DCPC) | 「民國95年網路教務組與交大出版社正式合併成『數位內容製作中心』」；校史館寫「教務處網路教務組、招生組、出版組調整為數位內容製作中心、綜合組」 | [S8][S7] | 一手（年份有落差） |
| 2007-02 | 教學發展中心 | 校史館 2007 年條目（和 E3 平台維運沒有直接關係） | [S7] | 一手（WebFetch 摘要） |
| 2017–2021 | DCPC 網站改到 aadm.nctu.edu.tw/dcpc（WordPress）；2021 年起頁首改稱「教學資源組 Division of Teaching Resources」 | 版權列「國立陽明交通大學 教學資源組」 | [S16] | 一手 |
| 2021– | 陽明交大教務處 教學資源組 → 「數位教學中心」 | E3 平台維運；e3cs@nycu.edu.tw；交大校區分機 31433、50152、50161 | [S27] | 一手 |

- Moodle theme 名稱 `dcpc` 就是 Digital Content Production Center 的縮寫，一路沿用到 e3.nycu.edu.tw 與 e3p 的 `dcpc2021.css`（一手字串＋推論）。

---

## 5. 圖片／截圖／文件線索

### 5.1 本次下載保存（`/Users/em/Desktop/nctu-e3-history/images/`）

| 檔名 | 內容 | 出處 |
|---|---|---|
| `2003_e-nctu_profile_image004.jpg` | E.NCTU 簡報投影片「緣起」（87–89 年計畫列表、八十九學年度推出 E.NCTU） | https://web.archive.org/web/2003id_/http://e.nctu.edu.tw/news/Profile.files/image004.jpg |
| `2003_e-nctu_profile_image006.jpg` | 投影片「E.NCTU 的特點」（資訊廣場、虛擬社群、個人工作室） | 同上 `image006.jpg` |
| `2003_e-nctu_profile_image010.jpg` | 投影片（系統平台架構） | 同上 `image010.jpg` |
| `2003_e-nctu_profile_image012.jpg` | 網路學習研究中心 logo／聯絡圖 | 同上 `image012.jpg` |
| `2006_e3_login_copyright_NCTU.gif` | E3 登入頁版權圖「版權所有 國立交通大學 Copyright © 2006」 | https://web.archive.org/web/20060503131837id_/http://e3.nctu.edu.tw:80/NCTU_E3/lms2/Images/Login/zh-TW/copyright.gif |
| `2007_e3ym_login_copyright_NCTU.gif` | 陽明 e3.ym.edu.tw 的同一張版權圖（仍是「國立交通大學」） | https://web.archive.org/web/20070713110452id_/http://e3.ym.edu.tw/E3/LMS2/Images/Login/zh-TW/copyright.gif |
| `wayback_2002-10-10_e2_eCampus_login.png` | e2 eCampus 登入頁（Wayback 渲染截圖，圖片部分缺失） | https://web.archive.org/web/20021010082927/http://e2.nctu.edu.tw:80/eCampus/default.aspx |
| `wayback_2006-07-03_e3_NCTU_E3_login.png` | 舊 E3 登入頁：「國立交通大學網路教學平台 v.3 / e-campus」（頁內新聞區為伺服器錯誤） | https://web.archive.org/web/20060703002931/http://e3.nctu.edu.tw/NCTU_E3/lms2/login.aspx |
| `wayback_2007-09-11_dcpc_home_E2_end_notice.png` | 數位內容製作中心首頁：E2 停止服務、e-Campus 3.0 教育訓練、e3同步上線公告 | https://web.archive.org/web/20070911051426/http://dcpc.nctu.edu.tw/ |
| `2017-09_NewE3_intro_OperationInstruction.pdf` | New E3 數位教學平台介紹（2017/09 版，27 頁，含大量系統截圖） | https://e3.nycu.edu.tw/theme/dcpc/doc/OperationInstruction/ |
| `2017-09_NewE3_intro_p1.png`、`2017-09_NewE3_intro_p3.png` | 上述 PDF 第 1 頁（定義段落）與第 3 頁（介面截圖）渲染圖 | 同上 |
| `wayback_2019-11-18_e3new_NewE3_login.png` | New e3 登入頁（CSS 未存檔，只有文字骨架） | https://web.archive.org/web/20191118090827/https://e3new.nctu.edu.tw/login/index.php |
| `wayback_2020-07-16_dcpc_e3_revised_107-2_notice.png` | dcpc 首頁「e3已於107下學期改版 請按此進入New e3使用」 | https://web.archive.org/web/20200716131006/http://dcpc.nctu.edu.tw/ |
| `2021-01-28_e3new_maintain.png` | e3new 維護頁圖「本系統，進行系統維護中 暫停服務，不便之處敬請見諒！」 | https://web.archive.org/web/20210128080945id_/https://e3new.nctu.edu.tw/maintain.png |
| `wayback_2021-01-30_e3nycu_login.png` | e3.nycu.edu.tw 首日登入頁 | https://web.archive.org/web/20210130053020/https://e3.nycu.edu.tw/login/index.php |
| `2023-09_E3workshop112-1_p7_old_platforms.png` | 112-1 E3 工作坊投影片第 7 頁「舊平台問題：eCampus、eeClass與NewE3(ym)」 | https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1161839994642370560&type=s |
| `wayback_2024-04-14_e3p_login.png` | e3p 最早存檔登入頁（新 logo「國立陽明交通大學 數位教學平台」） | https://web.archive.org/web/20240414071219/https://e3p.nycu.edu.tw/login/index.php |

（images 資料夾內其他 `e_*`、`e2_*`、`e3_*`、`live_*`、`logo_*` 檔案是其他筆記〔02、04〕產生的，不在本表。）

### 5.2 尚未下載、可再挖的圖片線索

- 官方手冊 PDF（內含大量 E3 截圖）：教務處「使用說明」清單 https://aa.nycu.edu.tw/aa/ch/app/data/list?module=nycu0130&id=2551
  - E3基本使用手冊(教師&助教) 2025.08.25（81 頁）
  - 教師＆助教版 2023.04（內文標 2022.Mar，52 頁）
  - 如何登入E3平臺與修改個人資料設定（2022-02-23，6 頁）
  - 112-1 E3 工作坊投影片（2023-09-22，59 頁）
  - E3New User manual for Basic Function（英文，內文 2020/1/10、2022.Oct，49 頁）
  - 以上已暫存在 scratchpad，未複製到 images
- Scribd：「交大New E3 Turnitin 學生版手冊 - 中文版 - 20190403」https://www.scribd.com/document/568437757/
- 舊 E3 內建使用手冊（有存檔）：`/NCTU_E3/lms2/UserManual/index.htm`（2006-07，「E3平台使用說明」目錄 23 項）、`UserManual/Common/Video/`、`UserManual/Student/`（2007）
- e2 說明：`/ECAMPUS_HELP/設定快顯封鎖程式.htm`（2005）、`/eCampus_Help/student/index.htm`（2006，「e-campus系統使用說明」）
- 陽明 eCampus：`e3.ym.edu.tw/ecampus3p/Learn/LoginPage2/product_login.aspx`（2015，有「eCampus使用說明手冊」「eCampus成績登錄使用說明書」連結）
- YouTube（頻道 @nycu_derek，楊宗瑋，數位教學中心）
  - 2021-03-18「110.03.18 E3 工作坊(一)」（合校後第一批工作坊，共四場 3/18、3/19、3/22、3/24）
  - 「1102 E3 教學平台工作坊(線上工作坊)」、「1111 E3 教學平台教育訓練工作坊(場次三)」（wz6yFM3ItSc）、「1112E3workshop」
  - 2024-03-28「1122 E3 新版教學工作坊(1)」（ZE79srnxgKg）、「20240328／20240329 112學年度第 2學期E3新版期中工作坊[搶鮮版]」（BglQN2327hA、yUcLuSRjEHM，2025-03-12 上傳）
  - 2024-05-02「從舊E3到新E3一次搬移整門課程-(字幕)」（I6noIrVd7y8）
  - 2024-05-20「如何從Moodle樣板切換回E3樣板」（U26CcVwYAv0）
  - 播放清單「數位工具」https://www.youtube.com/playlist?list=PLt29Ps7oS1RdwlnO6S9PNvtHtHjqu0mvO
- Google Play：NCTUe4 App 截圖（README 內 googleusercontent 圖）
- 校園公告附件「106下學期數位教學平台活動表.png」：https://bulletinboard.nycu.edu.tw/api/files/20180100289/ 下，目前抓不到（回傳 HTML）

---

## 6. GitHub／社群專案（反映系統世代與 URL 結構，皆二手）

| 專案 | 建立 | 對象 | 線索 |
|---|---|---|---|
| Spiderpowa/NCTU-E3MobileAPIDocument | 2013-09-17 | 舊 E3 | 「NCTU E3 System Mobile API Document」（對應 `mService/service.asmx`） |
| Spiderpowa/NCTU-E3X | 2013-09-17 | 舊 E3 | 「A modern E3 System」 |
| jay16213/e3plus | 2016-11-26 | — | 「a simple online learning platform with RoR, inspired by nctu e3」（名稱 e3plus，和官方無關） |
| Team214-tw/NCTUe4（Summon528） | 2018-03-12 | 舊 E3＋New E3 | 舊 E3 入口寫 `dcpc.nctu.edu.tw/index.aspx`，New E3 寫 `e3new.nctu.edu.tw/login/index.php` |
| mlouielu/e3dump | 2019-05-21 | New E3 | 「No worries about e3 shutdown」；目標 `e3new.nctu.edu.tw/local/courseextension/index.php` |
| wdzeng/NCTU-e3-Banner | 2019-06-17 | — | — |
| exodustw/NYCU-E3-CAPTCHA-Autowrite | 2021-07-31 | e3.nycu.edu.tw | 「autofill NYCU new E3 CAPTCHA」（e3.nycu 登入頁仍有驗證碼） |
| SiriusKoan/e3schedule | 2022-06-25 | e3.nycu | 用 session cookie 列作業 |
| junlinwk/e3cli、viecon/e3-cli、e3-extension、e3-mobile、NYCU-Chung/portal_e3_helper、elvisdragonmao/nycu-em3、jay900411/NYCU-Video-Controller | 2025–2026 | e3p | Moodle Web Service API；「NYCU e3p video player」 |
| ME₃GA-NCTU（mega.nctu.co） | — | E3 | 「專屬於交大學生的E3數位教學平台」非官方 App |

---

## 7. 論文、PTT、Dcard

- **學位論文**：在陽明交大機構典藏 DSpace API（`ir.lib.nycu.edu.tw/server/api/discover/search/objects`）以「E3平台」「eCampus」「E3系統」「網路教學平台 交大」「Moodle」「學習管理系統」「網路校園」等詞檢索，**沒有找到以交大 E3 為研究對象、且描述系統沿革的學位論文**。命中的只有不相關的 Moodle 研討會論文，以及 2001 年國科會計畫《網路教學系統平台與內容標準化規劃計畫》（曾憲雄，handle 11536/95997）。臺灣博碩士論文系統沒有能自動化查詢的介面，本次未能檢索 → 列為待補。
- **PTT**：限定 ptt.cc／pttweb.cc 搜尋，沒有找到相關討論串。
- **Dcard**（站方回 403，只有搜尋摘要，二手）
  - 「新的E3從哪裡進入」https://www.dcard.tw/f/nycu/p/254492628 （約 2024-01；e3p、newe3p）
  - 「新E3抱怨樓」https://www.dcard.tw/f/nctu/p/254787833
  - 「新e3平台真的很難用」https://www.dcard.tw/f/nctu/p/256640232
  - 「畢業之後還能登入e3嗎」https://www.dcard.tw/f/nycu/p/257586751
  - 「new e3網頁開很慢」https://www.dcard.tw/f/nycu/p/235865014
  - 「E3快速登入方法？」https://www.dcard.tw/f/nctu/p/239013817
- **部落格**：「New e3 數位教學平台 - 課程公告」https://nctu-freshman-orientation.blogspot.com/2020/09/new-e3.html （2020-09，新生入學輔導課程在 New e3 上，二手）

---

## 8. 未解問題／待查

1. 舊 E3 的開發分工：三趨科技和交大數位內容製作中心各負責哪些部分？有無採購案（政府電子採購網可查「eCampus」「三趨」決標紀錄）？
2. E2 是否確為三趨的五校 e-Campus？需要找 2002 年交大校訊或三趨新聞稿。
3. 舊 E3 正式關站日期與資料保存方式（「E3 線上學習系統（舊eCampus)」現在的實際網址）。
4. New E3 正式上線日（106 學年第 1 學期？），以及 107 下全面改版的官方公告原文（只找到 dcpc 首頁的連結文字）。
5. e3p 的正式公告（113 年 1–2 月期初工作坊公告）與「p」的由來；「E3+」是否只是俗稱。
6. 陽明 New E3（newe3.ym.edu.tw）公告原文：tss.ym.edu.tw 已無法解析，Wayback 也沒有收錄 `p/406-1006-42378`。
7. 交大教學發展中心《超薄型月刊》第 53 期 e3 介紹（academic.nctu.edu.tw/ctld/epaper/53/04-2.html）：網域已失效，Wayback 沒有收錄。
8. 校史館 2011-現今頁沒有任何 E3、New E3、e3p 的條目（已用全文比對確認）。

---

## 9. 來源清單

- [S1] 交大校史館「1991-2000 交大年表與大事記」https://museum.lib.nycu.edu.tw/?page_id=938 （一手）
- [S2] E.NCTU「Profile of E.NCTU」（網路大學推動小組 2000年獻禮）https://web.archive.org/web/20031204104846/http://e.nctu.edu.tw/news/Profile.htm ；最早版 https://web.archive.org/web/20010302091059/http://e.nctu.edu.tw/news/Profile.htm （一手）
- [S3] E.NCTU「第一次網路教材設計實務研習會」https://web.archive.org/web/20010309020357/http://e.nctu.edu.tw:80/news/news-1017.htm ；「網路學習研究中心」由來 https://web.archive.org/web/20010615002334/http://e.nctu.edu.tw:80/news/news20010419.htm ；停機公告 https://web.archive.org/web/20010505014231/http://e.nctu.edu.tw:80/news/news20010425.htm （一手）
- [S4] e2 eCampus 登入頁 https://web.archive.org/web/20021010082927/http://e2.nctu.edu.tw:80/eCampus/default.aspx ；最新消息 https://web.archive.org/web/20021210043226/http://e2.nctu.edu.tw:80/eCampus_GuestView/sys_new_view.aspx （一手）
- [S5] 三趨科技股份有限公司「公司簡介／沿革」http://www.3probe.com.tw/about_milestone.aspx ；產品頁 https://www.3probe.com.tw/products_el.aspx （一手，廠商自述）
- [S6] E.NCTU 站內最新消息 `Board/news/query2.php?id=13…24`，例：https://web.archive.org/web/20021231102242/http://e.nctu.edu.tw:80/Board/news/query2.php?id=19 （一手，Big5）
- [S7] 交大校史館「2001-2010」https://museum.lib.nycu.edu.tw/?page_id=940 （一手）
- [S8] 數位內容製作中心「關於我們－服務項目」https://web.archive.org/web/20070917181432/http://dcpc.nctu.edu.tw:80/aboutus_01.htm ；「成員執掌」https://web.archive.org/web/20071002070515/http://dcpc.nctu.edu.tw:80/aboutus_03.htm ；「教學平台介紹（e-campus 簡介、E3 新功能說明）」https://web.archive.org/web/20071002070551/http://dcpc.nctu.edu.tw:80/instruction_01.htm （一手）
- [S9] 數位內容製作中心首頁 2007-09-11 https://web.archive.org/web/20070911051426/http://dcpc.nctu.edu.tw/ （一手）
- [S10] 數位內容製作中心「教學平台介紹（e-campus 及 i-CT 簡介）」https://web.archive.org/web/20170829185813/http://aadm.nctu.edu.tw:80/dcpc/?page_id=173 （一手）
- [S11] 《New E3 數位教學平台 介紹 2017/09 版》https://e3.nycu.edu.tw/theme/dcpc/doc/OperationInstruction/ （一手，PDF）
- [S12] 陽明交大校園公告系統 id=20180100289（「106下學期數位平台活動預告」）https://infonews.nycu.edu.tw/index.php?topflag=1&SuperType=2&SuperTypeNo=2&type=%EF%BF%BD%C7%B3N&id=20180100289&action=detail （內文已不存在，引文來自搜尋摘要，二手）
- [S13] dcpc.nctu.edu.tw 首頁 2020-07-16 https://web.archive.org/web/20200716131006/http://dcpc.nctu.edu.tw/ 、2021-01-11 https://web.archive.org/web/20210111183640/http://dcpc.nctu.edu.tw/ （一手）
- [S14] 陽明教學資源組「New E3數位教學教學平台於109年2月17日正式上線」https://tss.ym.edu.tw/p/406-1006-42378,r1.php?Lang=zh-tw （網域已失效，標題與摘要來自搜尋結果，二手）
- [S15] 陽明大學「在校學生」頁 https://web.archive.org/web/20210803045133/http://web.ym.edu.tw/files/11-1133-1940.php ；ee-class 首頁 https://web.archive.org/web/20171101141521/http://eeclass.ym.edu.tw/ ；陽明 eCampus https://web.archive.org/web/20150120004521/http://e3.ym.edu.tw:80/ecampus3p/Learn/LoginPage2/product_login.aspx 、https://web.archive.org/web/20061026102258/http://e3.ym.edu.tw:80/E3/LMS2/default.aspx （一手）
- [S16] 教學資源組（原數位內容製作中心）「新版e3」2020-07-28 https://web.archive.org/web/20211201215725/https://aadm.nctu.edu.tw/dcpc/?p=471 （一手）
- [S17] 交大校史館「2011-現今」https://museum.lib.nycu.edu.tw/?page_id=942 （一手）
- [S18] 陽明交大教務處【E3 問答集】教師篇（110-02-24）https://aa.nycu.edu.tw/aa/ch/app/news/view?module=headnews&id=2652&serno=30895784-2cd7-458f-9856-9ecc78ff8668 （一手）
- [S19] 112-1 E3教學平臺工作坊投影片 https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1161839994642370560&type=s （一手）
- [S20] 舊 E3 存檔頁：https://web.archive.org/web/20060227235201/http://e3.nctu.edu.tw/NCTU_E3/lms2/Default.aspx 、https://web.archive.org/web/20090216090058/http://e3.nctu.edu.tw/NCTU_E3P/lms2/ 、https://web.archive.org/web/20061215082709/http://e3.nctu.edu.tw/NCTU_E3/lms2/login_news.aspx?Language=zh-TW 、https://web.archive.org/web/20060703003231/http://e3.nctu.edu.tw/NCTU_E3/lms2/UserManual/index.htm ；GitHub https://github.com/Spiderpowa/NCTU-E3MobileAPIDocument （一手／二手）
- [S21] Dcard「新的E3從哪裡進入」https://www.dcard.tw/f/nycu/p/254492628 （二手）
- [S22] YouTube：https://youtu.be/ZE79srnxgKg 、https://youtu.be/BglQN2327hA 、https://youtu.be/yUcLuSRjEHM 、https://youtu.be/I6noIrVd7y8 、https://youtu.be/U26CcVwYAv0 、https://youtu.be/d2b3KqJ5-4M （一手，數位教學中心承辦人頻道）
- [S23] 問答「從舊E3到新E3一次搬移整門課程」（114-03-26）https://www.nycu.edu.tw/aa/ch/app/data/view?module=nycu0037&id=2883&serno=6377c04d-12ba-44ca-9307-6e1686ce8743 （一手）
- [S24] 「E3網站使用協議」https://www.nycu.edu.tw/aa/ch/app/news/view?module=headnews&id=2652&serno=90192ef6-b891-4d76-87cf-a55203d8c048 （一手）
- [S25] 曾憲雄《網路教學系統平台與內容標準化規劃計畫》https://ir.lib.nycu.edu.tw/handle/11536/95997 （一手書目）
- [S26] 「如何登入E3平臺與修改個人資料設定」https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1161841314002636800&type=s ；「E3基本使用手冊 教師＆助教版（2023.04）」https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1161841516017094656&type=s ；2025.08.25 版 https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1423113266715955200&type=s ；英文版 https://www.nycu.edu.tw/aa/ch/app/data/doc?module=nycu0130&detailNo=1161841693712977920&type=s （一手）
- [S27] 數位教學中心「單位簡介」https://aa.nycu.edu.tw/aa/ch/app/artwebsite/view?module=artwebsite&id=2546&serno=ef67c2e1-568e-4e99-95de-5dfab6a55a2d （一手）
- [S28] 問答「e3 登入驗證方式，增加"手機驗證方法"」https://aa.nycu.edu.tw/aa/ch/app/data/view?module=nycu0037&id=2564&serno=7d74adb3-7517-4b5f-9ebd-de869b75b64c （一手）
- 其他存檔：
  - e3new 登入頁 https://web.archive.org/web/20191118090827/https://e3new.nctu.edu.tw/login/index.php
  - e3new 維護頁 https://web.archive.org/web/20210128080940/https://e3new.nctu.edu.tw/
  - e3.nycu 首日 https://web.archive.org/web/20210130053020/https://e3.nycu.edu.tw/login/index.php
  - e3p 首次 https://web.archive.org/web/20240414071219/https://e3p.nycu.edu.tw/login/index.php
  - DCPC WordPress 首頁 https://web.archive.org/web/20210307031156/http://aadm.nctu.edu.tw/dcpc/
  - Wayback CDX API：`https://web.archive.org/cdx/search/cdx?url=<host>&matchType=host`
