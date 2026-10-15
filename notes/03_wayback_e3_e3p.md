# 03 — Wayback 考古：舊 E3、New E3、e3.nycu、e3p（2006–2026）

> 範圍：`e3.nctu.edu.tw`（舊 E3）、`e3new.nctu.edu.tw`（New e3）、`e3.nycu.edu.tw`、`e3p.nycu.edu.tw`，以及實際承載 E3 入口與公告的 `dcpc.nctu.edu.tw`（交大教務處數位內容製作中心）。
> 方法：Wayback CDX 全量清單 → 依 digest 去重 → 用 `id_` 抓原始 HTML（Big5 頁面以 cp950 解碼）→ 比對 `<title>`、HTTP 標頭（`x-archive-orig-*`）、Moodle `M.cfg` 鍵值、theme／YUI 路徑。Moodle 版本以 GitHub 上 `moodle/moodle` 各 `MOODLE_xxx_STABLE` 分支的 `outputrequirementslib.php`／`page_requirements_manager.php` 實際比對 `M.cfg` 鍵值集合。
> 記號：**【確認】** = 存檔頁面原文或標頭直接可見；**【推測】** = 由間接證據推論，可能有誤。
> 調查日：2026-10-16。

---

## 0. 一頁總覽（時間軸）

| 時間 | 事件 | 依據 |
|---|---|---|
| 2006-02-24 | 舊 E3 最早可見版本：`NCTU_E3/lms2/Default.aspx`，title `NCTU E3 (v1.2006.0224.30796)` | 【確認】[2006-02-27 存檔](https://web.archive.org/web/20060227235201/http://e3.nctu.edu.tw:80/NCTU_E3/lms2/Default.aspx) |
| 2006-06/07 | 系統名稱改為 **eCampus III**（title `eCampus III v1.1.60629.38870`） | 【確認】[2006-07-03](https://web.archive.org/web/20060703002854/http://e3.nctu.edu.tw:80/NCTU_E3/lms2/Default.aspx) |
| 2007-08-16 | 公告「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」 | 【確認】[dcpc 2007-09-11](https://web.archive.org/web/20070911051426/http://dcpc.nctu.edu.tw:80/) |
| 2007–2008 | 「e-Campus 3.0 網路教學平台教育訓練」多次開課 | 【確認】dcpc 首頁 |
| 2008-09 起 | `e3.nctu.edu.tw/` 根目錄改 302 轉到 `dcpc.nctu.edu.tw`（入口與登入框改放在數位內容製作中心網站） | 【確認】Wayback 標頭 |
| 2009-02-16 | 系統升級為 v1.5，路徑改為 `NCTU_E3P/LMS2/` | 【確認】[2009-02-16](https://web.archive.org/web/20090216234211/http://e3.nctu.edu.tw:80/NCTU_E3P/LMS2/Default.aspx) |
| 2010-09-13/16 | 路徑再改為 `NCTU_EASY_E3P/LMS2/`；dcpc 公告「好康訊息！新e3上線」 | 【確認】CDX 首見 2010-09-13；公告 2010/09/16 |
| 2014-06-27 | 公告「舊版 e3 將於9月1日【停止服務】」 | 【確認】[dcpc 2014-07-07](https://web.archive.org/web/20140707004421/http://dcpc.nctu.edu.tw/) |
| 2016-09 | 路徑改為 `NCTU_EASY_E3P/LMS3/`（程式版號仍是 `eCampus III v1.5.02193.01450`） | 【確認】CDX、[LMS3 根目錄 2016-09-15](https://web.archive.org/web/20160915122444/http://e3.nctu.edu.tw:80/NCTU%5FEasy%5FE3P/lms3/) |
| 2017-09-27 | dcpc 公告「New E3網址 http://e3.nctu.edu.tw/new」→ 轉到 `e3new.nctu.edu.tw`（Moodle）；新舊 E3 開始並行 | 【確認】[dcpc 2017-12-19](https://web.archive.org/web/20171219093122/http://dcpc.nctu.edu.tw/) |
| 2017-12-14 | 「New e3 12/19(二) 停機公告」 | 【確認】同上 |
| 2018-06 | 舊 E3 路徑改為 `NCTU_EASY_E3P/LMS31/`；伺服器由 IIS 6.0 換成 IIS 8.5 | 【確認】CDX、標頭 |
| 2019-02（107 學年度下學期） | **E3 正式改版為 New e3**（dcpc 首頁：「e3已於107下學期改版／請按此進入New e3使用」） | 【確認】文字見 [dcpc 2020-05-26](https://web.archive.org/web/20200526020638/https://dcpc.nctu.edu.tw/) 起 |
| 2019-09 | 舊 E3（LMS31）最後一批 200 存檔（2019-09-14），2019-09-29 已回 401；LMS3 自 2019-01 起大量 404 | 【確認】CDX |
| 2019-10 ~ 2020-10 | 舊 E3 停機；確切日期查無公告。下一筆存檔 2020-10-25 已是 404 | 【推測】 |
| 2021-01-28 | e3new 顯示維護頁 `maintain.png`（「本系統，進行系統維護中，暫停服務」） | 【確認】[2021-01-28](https://web.archive.org/web/20210128080940/https://e3new.nctu.edu.tw/) |
| 2021-01-29/30 | `e3.nycu.edu.tw` 出現（themerev = 2021-01-29 15:10；首筆存檔 2021-01-30）；頁尾改為「國立陽明交通大學 教學資源組」 | 【確認】 |
| 2021-05 前 | `e3new.nctu.edu.tw` → 301 → `https://e3.nycu.edu.tw/` | 【確認】2021-05-25 存檔標頭 |
| 2021-08 ~ 2022-02 | e3.nycu 升級 Moodle（3.3–3.7 → 3.8–3.10） | 【確認】M.cfg 鍵值變化；版本範圍為【推測】 |
| 2022-03 前 | 登入頁改成「僅供校外使用者」＋Google Authenticator 二階段驗證；`e3.nctu.edu.tw/` 改 302 → `e3.nycu.edu.tw` | 【確認】 |
| 2024-01-08 ~ 2024-02-26 | e3.nycu 登入頁加入 `<meta http-equiv="refresh" content="0; url=https://e3p.nycu.edu.tw/">` | 【確認】2024-02-26 存檔已有，2023-12-08 存檔沒有 |
| 2024-02-23 | e3p 的 jsrev（最早的 JS 快取版本）= 2024-02-23；首筆存檔 2024-04-14 | 【確認】數值；上線時間為【推測】 |
| 2024-06-24 | e3p 升級（Moodle 4.0 → 4.1–4.3） | 【推測】依 M.cfg |
| 2025-03 ~ 2025-11 | e3p 升級到 Moodle ≥ 4.5（YUI 3.18.1；M.cfg 多出 `apibase`／`siteId`／`userId`） | 【推測】依 M.cfg |
| 2026-10（現況） | e3.nycu 與 e3p 都還在線；e3.nycu 登入頁 0 秒轉到 e3p | 【確認】live 測試 |

---

## 1. 舊 E3：`e3.nctu.edu.tw`（2006–2019）

### 1.1 系統名稱
- **官方產品名：`eCampus III`**【確認】。`Default.aspx` 的 `<title>` 從 2006-07 起固定為 `eCampus III v<版號>`；在這之前（2006-02 ~ 2006-05）是 `NCTU E3 (v1.2006.0224.30796)` 這種寫法。
- 對外稱呼：「交大e-Campus（簡稱e3）網路教學平台」【確認，dcpc 2007/2008 新聞頁】、「e-Campus 3.0 網路教學平台」【確認，教育訓練公告】、登入頁橫幅「國立交通大學網路教學平台 v.3」＋「e-campus」logo【確認，見截圖】。
- 「E3」= e-Campus 第 3 代（前一代為 E2，2007-09 底停止服務）【確認，dcpc 2007-08-16 公告】。

### 1.2 開發／維運單位
- **教務處「數位內容製作中心」（Digital Content Production Center，DCPC；2010 年後英文改為 Center for Digital Content Production）**【確認】。依據：
  - DCPC「服務項目」頁列出「**網路教學平台的開發與維運**」、「平台內全校課程的建置、全校老師與學生的帳號建立」、「平台功能的使用諮詢」【確認，[dcpc aboutus_01 2007-09-17](https://web.archive.org/web/20070917181432/http://dcpc.nctu.edu.tw:80/aboutus_01.htm)】。
  - 2008-09 起 `e3.nctu.edu.tw/` 直接 302 到 `dcpc.nctu.edu.tw`，E3 的登入框、公告都放在 DCPC 首頁；DCPC 首頁標題列寫「e3網路教學平台登入」。
  - 公告署名「數位內容製作中心 e3團隊」【確認，2015/4/16 公告】。
  - E3 系統信寄件人 `cdcp_notice@nctu.edu.tw`【確認】。
- **外包廠商**：在所有抓到的頁面、版權圖、title 中都**沒有看到任何廠商名稱**。版權字樣一律是「版權所有 國立交通大學 Copyright © 2006 National Chiao Tung University」（圖片 `copyright.gif`）與「Copyright 2006/2010 by NCTU Digital Content Production Center」。
  - 【推測】結合 DCPC 自述「開發與維運」、版號像 .NET 組件版本自動流水號（例如 `v1.4.11258.20860`，第三段 = 月日＋年尾數，第四段 = 秒數式 build number）、以及頻繁到數天一版的 build，**較可能是 DCPC 自行開發（或至少自行持有原始碼並持續建置）**。不排除最初有委外，但存檔中查無佐證。
- 計中（資訊技術服務中心）只在 DCPC 公告中以「機房電力維護」「網頁防火牆調整」等角色出現；2015 年 e3 教育訓練借用計中訓練教室。沒有證據顯示計中是 E3 的開發單位。教發中心在本批存檔中未出現。

### 1.3 技術
| 項目 | 觀察 | 依據 |
|---|---|---|
| 平台 | ASP.NET（`.aspx`、`.ashx`、`.asmx`、`WebResource.axd`、`__VIEWSTATE`、`__EVENTVALIDATION`） | 【確認】CDX 副檔名統計：aspx 14,396 筆、ashx 277、asmx 92、axd 77 |
| Web 伺服器 | `Microsoft-IIS/6.0` + `X-Powered-By: ASP.NET`（2006–2017）；`Microsoft-IIS/8.5`（2018-08 起） | 【確認】`x-archive-orig-server` 標頭 |
| AJAX | Anthem.NET（`var Anthem_FormID = "Form1"`），`Microsoft.XMLHTTP` ActiveX 做 session keep-alive（`common_session_life_detector.aspx`） | 【確認】login.aspx 原始碼 |
| 前端 | frameset（`Default.aspx` 包 `login.aspx`）、整頁切圖（`Images/Login/zh-TW/login_02.gif` 等）、Dreamweaver `MM_swapImage` 滑鼠換圖 | 【確認】 |
| 瀏覽器 | 「本平台目前僅適用IE, 使用其它的Browser無法保証所有功能皆能正常執行」 | 【確認】[login_news 2006-12-15](https://web.archive.org/web/20061215082709/http://e3.nctu.edu.tw:80/NCTU_E3/lms2/login_news.aspx?Language=zh-TW) |
| 行動 API | `/mService/service.asmx`（例如 `?op=GetSystemNewsDetail`，2016-04） | 【確認】CDX；【推測】是 iNCTU App／iCT 行動平台用的 Web Service |
| 單一登入 | `login_sso.aspx`（2013 存檔中出現）；2018 DCPC 登入框有「由交大入口網站登入」按鈕 | 【確認】 |
| generator meta | 無 `<meta name="generator">` | 【確認】 |

### 1.4 路徑／版本世代
| 期間（CDX） | 應用程式路徑 | `<title>` 版號 | 備註 |
|---|---|---|---|
| 2006-02 ~ 2009-01 | `/NCTU_E3/lms2/` | `NCTU E3 (v1.2006.0224…)` → `eCampus III v1.1.6xxxx` → v1.2（2006-11）→ v1.3（2007-01）→ v1.4（2007-09）| 2006-02-24 首版 |
| 2009-02 ~ 2011-10 | `/NCTU_E3P/LMS2/` | `eCampus III v1.5.02169.01430`（2009-02-16）起 | 【推測】「E3P」可能是 E3 Plus／Pro 之類，存檔無解釋 |
| 2010-09 ~ 2016 | `/NCTU_EASY_E3P/LMS2/` | v1.5.09130.01330（2010-09-13）… 最後 `v1.5.02193.01450`（build 2013-02-19，一直用到 2016） | 對應 2010/09/16「新e3上線」公告 |
| 2016-09 ~ 2019-09 | `/NCTU_EASY_E3P/LMS3/` | 仍是 `v1.5.02193.01450` | 只是換部署目錄 |
| 2018-06 ~ 2019-09 | `/NCTU_EASY_E3P/LMS31/` | （Default.aspx 未存到） | IIS 8.5 |

完整 `Default.aspx` title 序列（共 60 餘個版本）見附錄 A。

### 1.5 UI 改版
- **登入頁（login.aspx）2006–2012 幾乎沒變**：橫幅「國立交通大學網路教學平台 v.3」＋綠色 e-campus 主視覺、橘色帳密框、右側選單（最新消息／相關連結／平台介紹／常見問題／與我們連絡）。比對 Wayback digest：`login_02.gif`、`login_03.gif`、`login_10.gif`、`login_12.gif`、`login_21.gif` 在 2006 與 2012 的 SHA1 完全相同【確認】。2012 版只拿掉「簡体中文版」按鈕，「與我們連結」改成「連絡我們」。
- **實際入口改到 DCPC 首頁**（2008-09 起）：
  - 2007–2008 版 DCPC 首頁：左側「國立交通大學網路教學平台 e-Campus」登入框（中文／英文／簡體三語）。
  - 2010 年 DCPC 改版：右側藍色 e-Campus 登入框（中文／English），「Forgot Password / Guest / FAQ」。
  - 2017 年底起登入框多出「由交大入口網站登入（Logging from Portal）」按鈕。
  - 2020 年存檔：登入框換成文字「e3已於107下學期改版／請按此進入New e3使用／本校師生仍可透過單一入口登入。」
- 2016–2019 的 LMS3／LMS31 登入切圖沒被 Wayback 存到，無法重現當時的登入頁畫面。

### 1.6 重要公告（摘錄）
> 以下公告都在 DCPC 網站（E3 的實際入口）。舊 E3 自己的 `login_news.aspx` 除了 2006-12 那一則以外，存到的都是空白。

- 2006/11/21「使用e-Campus平台，請務必設好IE Browser之安全性與快顯封鎖設定。」
- 2007/09/07「e3同步、e3同步上線了！敬請各位上e3網路教學平台一探究竟～」— [dcpc 2007-09-11](https://web.archive.org/web/20070911051426/http://dcpc.nctu.edu.tw:80/)
- 2007/08/16「**E2網路教學平台提供服務至九月底止，請教師們轉用E3平台**」— 同上
- 2007/08/30「9月6日 10:00~12:00【e-Campus 3.0 網路教學平台教育訓練課程】」— 同上
- 2007 新聞頁：「*交大e-Campus（簡稱e3）網路教學平台：http://e3.nctu.edu.tw/」— [news_show 2007-11-15](https://web.archive.org/web/20071115175845/http://dcpc.nctu.edu.tw:80/news_show.aspx?id=ef8810ab-536f-4cf5-9932-e8ee96cd1e5b)
- 2007 平台介紹頁「E3 新功能說明：使用者可隨時切換三種語系（繁體中文、英文、簡體中文）頁面；有課程旁聽功能、訪客參觀功能；提供公式輸入工具、線上文章編輯工具…」— [instruction_01 2007-10-02](https://web.archive.org/web/20071002070551/http://dcpc.nctu.edu.tw:80/instruction_01.htm)
- 2010/09/16「**好康訊息！新e3上線**，功能更多、使用更便利，教師及助教請利用課程裡的「進階設定」開啟相關功能」— [dcpc 2010-10-21](https://web.archive.org/web/20101021205425/http://dcpc.nctu.edu.tw:80/)
- 2011/02/23「e3平台 - 如何從舊版換回新版？［e3舊換新-操作說明］」— [dcpc 2011-05-16](https://web.archive.org/web/20110516153702/http://dcpc.nctu.edu.tw:80/)
- 2013/02/21「您的e3功能太簡易了嗎？其實e3有進階功能哦！教師及助教可利用課程裡的「進階設定」開啟相關功能。」— [dcpc 2013-03-26](https://web.archive.org/web/20130326103213/http://dcpc.nctu.edu.tw/)
  - 【推測】路徑中的「EASY」對應 2010 年新 e3 預設的「簡易」介面，進階功能要另外開啟。
- 2013/02/23「大交大．小雲端．微學習 － 交大行動學習平台iCT」
- 2014/06/27「**舊版 e3 將於9月1日【停止服務】**，詳細內容請見附件」— [dcpc 2014-07-07](https://web.archive.org/web/20140707004421/http://dcpc.nctu.edu.tw/)（附件 `getFile.aspx` 沒有存檔；「舊版」指的是哪個路徑無法確定，【推測】是 2010 年以前的 `NCTU_E3P` 介面）
- 2016/09/10「e3 / iNCTU ID & Password：第一次登入者，帳號密碼同選課系統。」（2020 年版消息列表）
- 2017/09/27「**New E3網址 http://e3.nctu.edu.tw/new**」（連結經 `action.aspx` 傳導頁 → `e3.nctu.edu.tw/new` → 302 → `http://e3new.nctu.edu.tw/`）— [dcpc 2017-12-19](https://web.archive.org/web/20171219093122/http://dcpc.nctu.edu.tw/)、[/new 轉址 2018-01-01](https://web.archive.org/web/20180101231236/http://e3.nctu.edu.tw:80/new/)
- 2017/10/11「iNCTU App 下架說明：本學期起iNCTU APP 因應系統維運規劃正式下架，不再提供服務，如欲使用E3數位教學平台，請由學校首頁，點選教職員/學生界面，選擇進入E3教學平台即可。」— [news 2020-09-23 存檔](https://web.archive.org/web/20200923181458/https://dcpc.nctu.edu.tw/news_show.aspx?id=83b37347-3c45-4f6f-aa82-01036a4cd1af)
- 2017/12/14「New e3 12/19(二) 停機公告」— [dcpc 2017-12-19](https://web.archive.org/web/20171219093122/http://dcpc.nctu.edu.tw/)
- 2018 起 DCPC 首頁的新聞改為連到 `https://e3new.nctu.edu.tw/theme/dcpc/news/news_view.php?d=…`（New e3 內建的公告系統；這些頁面沒有存檔）【確認，連結存在於 2018-01、2019-07 首頁】。
- 2020（最早見於 2020-05-26）DCPC 首頁登入框改成：「**e3已於107下學期改版**／請按此進入New e3使用（→ https://e3new.nctu.edu.tw）／本校師生仍可透過單一入口登入。」— [dcpc 2020-05-26](https://web.archive.org/web/20200526020638/https://dcpc.nctu.edu.tw/)（2019-07-20 版還沒有這段字，所以是 2019-07 ~ 2020-05 之間加的）

### 1.7 新舊並行與停用
- **並行期**：2017-09（New E3 網址公告）到 2019-09（舊 E3 最後的 200 回應）【確認】。
- **正式切換**：107 學年度下學期（2019-02）【確認，依 DCPC 文字；但這段字只在 2020 年的存檔看得到】。
- **停用日**：沒有找到明確的「舊 E3 停用」公告。CDX 顯示 LMS31 到 2019-09-14 都還有 200，2019-09-29 回 401；之後到 2020-10-25 都沒有存檔，2020-10 再存到時已是 404【確認】。所以停用時間落在 **2019-09-29 ~ 2020-10-25** 之間【推測】。
- 根網域 `e3.nctu.edu.tw/` 到 2021-04-12 都還 302 到 DCPC 首頁，2022-03-19 起改為 302 到 `https://e3.nycu.edu.tw/`【確認】。

---

## 2. New e3：`e3new.nctu.edu.tw`（2017-09 ~ 2021-01）

### 2.1 是否 Moodle：是【確認】
- `M.cfg = {"wwwroot":"https:\/\/e3new.nctu.edu.tw",…,"theme":"dcpc","iconsystemmodule":"core\/icon_system_fontawesome",…}`、`MoodleSession` cookie 說明、`moodle-core-*` YUI 模組、`/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css`、`/pluginfile.php/1/core_admin/logo/…`。
- **佈景：`theme_dcpc`**（自製，以 DCPC 命名；`theme/styles.php/dcpc/<rev>/all`）【確認】。
- 外掛：`auth/googleoauth2`（Google OAuth2 登入外掛）【確認】。
- body class：`yui3-skin-sam e3new-nctu-edu-tw pagelayout-login`【確認】。

### 2.2 版本判斷
- `M.cfg` 鍵值集合 = `wwwroot sesskey themerev slasharguments theme iconsystemmodule jsrev admin svgicons usertimezone contextid`。
- 與 Moodle 原始碼比對：3.2 沒有 `iconsystemmodule`／`usertimezone`；3.3、3.4、3.5、3.6、3.7 都正好是這 11 個鍵；3.8 起多了 `sessiontimeout`、`langrev`、`templaterev`。
- ⇒ **Moodle 3.3 ~ 3.7**【推測，但證據很強】。YUI 3.17.2 與這個範圍相符。
- 站名（`<title>`）：「**New e3 數位教學平台**: 登入本網站」【確認】。
- Logo 檔：`NewE3Cloud_orange_w.png`（橘色雲朵＋「國立交通大學 數位教學平台」）【確認】，存為 `images/logo_e3new_NewE3Cloud_orange_w.png`。
- 頁尾：「Copyright ©2018 國立交通大學 數位內容製作中心 版權所有」【確認】。
- 登入頁：帳號／密碼／CAPTCHA、「校內使用者忘記密碼」「校外使用者忘記密碼」、「（提醒：本校人員請使用單一入口帳號密碼）」【確認】。

### 2.3 時間
- themerev／jsrev：2019-07-10、2019-10-17、2020-08-05（Unix 時間戳換算，Asia/Taipei）【確認數值】。
- 首筆存檔 2017-11-01（root 302，內容未存）；可讀的登入頁從 2019-07-20 開始【確認】。DCPC 在 2017-09-27 公告 New E3 網址【確認】。
- ⇒ **上線約在 2017-09（106 學年度上學期）**【推測】；與舊 E3 並行到 2019-09。
- 2021-01-28：首頁換成維護圖 `maintain.png`（「本系統，進行系統維護中 暫停服務，不便之處敬請見諒！」）【確認】→ 這時正在搬到 `e3.nycu.edu.tw`。
- 2021-05-25 起：`e3new.nctu.edu.tw/` → 301 → `https://e3.nycu.edu.tw/`（nginx）【確認】。

---

## 3. `e3.nycu.edu.tw`（2021-01 ~ 現在）

### 3.1 就是 e3new 搬過來的【確認／高度可信】
- 同一套 Moodle：佈景同為 `theme_dcpc`、同一個 logo 檔名 `NewE3Cloud_orange_w.png`、同樣的登入頁版面（藍框＋黃色登入鈕）、相同的 `M.cfg` 鍵值集合（2021-01 ~ 2021-09）、同樣用 `auth/googleoauth2`。
- 時間連續：e3new 2021-01-28 維護頁 → e3.nycu themerev = **2021-01-29 15:10** → 首筆存檔 2021-01-30。陽明交大在 2021-02-01 合校，換網域的時間點剛好在合校前幾天。
- 改的部分：站名從「New e3 數位教學平台」改成「e3 數位教學平台」（2021-09 起寫成大寫「E3 數位教學平台」）；logo 文字改成「國立陽明交通大學 數位教學平台」；頁尾改為「**Copyright ©2021 國立陽明交通大學 教學資源組 版權所有**」（單位名稱由「數位內容製作中心」改為「教學資源組」）【確認】。

### 3.2 Moodle 版本與佈景
| 期間 | M.cfg 特徵 | 判斷 |
|---|---|---|
| 2021-01 ~ 2021-09 | 與 e3new 相同的 11 個鍵 | Moodle 3.3–3.7【推測】 |
| 2022-03 ~ 2026 | 多出 `sessiontimeout`、`langrev`、`templaterev`；沒有 `sessiontimeoutwarning`、`homeurl` | **Moodle 3.8–3.10**【推測】；升級時間在 2021-08-06 ~ 2022-02-14 之間（themerev 2022-02-14） |

- 佈景一直是 `theme_dcpc`（CSS `theme/dcpc/style/dcpc2021.css?20211025`）；YUI 3.17.2。
- themerev 演進：2021-01-29 → 2021-04-16 → 2021-08-06 → 2022-02-14 → 2022-10-26 → 2023-01-16 → 2023-09-25 → 2024-01-08 → **2024-07-15（之後到 2026-04 都沒有再變）**。

### 3.3 登入頁公告（摘錄）
- 2021：「（提醒：本校人員請使用單一入口帳號密碼）」— [2021-01-30](https://web.archive.org/web/20210130053020/https://e3.nycu.edu.tw/login/index.php)
- 2022-03 起「登入說明」：「本登入頁僅供校外使用者（含學分班學生、校際選修）進入；本校師生、職員，請由【單一入口】進入。校外使用者帳號以二階段認證的方式登入，初次登入者，本平台將寄出電子郵件，內含帳號、密碼及16字的Google Authenticator設定金鑰。」— [2022-03-08](https://web.archive.org/web/20220308074705/https://e3.nycu.edu.tw/login/index.php)
- 單一入口連結：`https://portal.nycu.edu.tw/#/login?redirect=%2Fredirect%2Fnewe3`、`https://portal.nycu.edu.tw/portal/newe3`；二階段驗證說明書放在教務處網站 `aa.nycu.edu.tw/ddl_post/【e3平台】二階段驗證使用說明書/`【確認】。

### 3.4 現在變成什麼（與 e3p 的關係）
- **2024-02-26 起的存檔**，登入頁 `<head>` 第一行就是 `<meta http-equiv="refresh" content="0; url=https://e3p.nycu.edu.tw/" />`；2023-12-08 的存檔還沒有【確認】。themerev 在 2024-01-08 更新，【推測】轉址是這個時候加上的。
- 2026-10-16 live 測試：`https://e3.nycu.edu.tw/` → 303 → `/login/index.php`（nginx，Moodle 本身還在跑），頁面仍帶上述 meta refresh，瀏覽器會立刻跳到 e3p【確認】。
- CDX 有 2024-07 ~ 2025-03 的 `course/view.php?id=…` 存檔（303 轉到登入），表示課程頁網址還在【確認】。
- 單一入口同時保留兩個代號：`portal/newe3`（e3.nycu）與 `portal/newe3p`（e3p；見 e3p 登入頁連結）【確認】。
- ⇒ 【推測】**e3.nycu 變成「舊學期課程的封存／查詢站」**：未登入的人（尤其校外帳號）一律被導到 e3p；校內師生仍可從單一入口 `newe3` 進入看 2023 學年度以前的課程。存檔中**沒有**找到明說「歷史課程封存」的公告，這一點需要校方文件佐證。

---

## 4. `e3p.nycu.edu.tw`（2024 ~ 現在，現行 E3）

### 4.1 名稱
- `<title>`：「登入本網站 | **E3@NYCU**」（網站簡稱）；登入框：「Log in to **E3數位教學平台**」【確認】。
- **「e3p」的 p 代表什麼：存檔中沒有任何解釋**【確認：查無】。
  - 舊 E3 在 2009–2019 年的路徑就叫 `NCTU_E3P`／`NCTU_EASY_E3P`，所以「E3P」這個字串在交大已用了十幾年【確認】。
  - 【推測】可能是 E3 Plus／新版之意，或只是為了跟同時在線的 `e3` 主機區分。沒有證據，不要當成定論。

### 4.2 技術平台
- **Moodle**，佈景 **`theme_boost_union`**（Boost Union，社群的 Boost 子佈景）【確認：`theme/styles.php/boost_union/…`、`pluginfile.php/1/theme_boost_union/logo/…`】。
- 有 `local/csp`（CSP 外掛）路徑（e3.nycu 上也有 `local/csp/collector.php`）、`proctoring_pro_logo.png`（線上監考外掛）【確認：CDX】。
- 沿用 e3 的視覺：藍框＋黃色登入鈕＋橘色雲朵 logo（`NewE3Cloud_orange_w.png`，2025-12 起改成 `E3Cloud_orange_w.png`）；甚至載入 `theme/dcpc/style/dcpc2021.css?20211025`【確認】→ 可見是同一個團隊延續原本的設計。
- 校外帳號驗證改成「輸入帳號密碼後，您的Email信箱會收到6位數字驗證碼」（e3.nycu 是 Google Authenticator）；有「以訪客身分登入」【確認】。

### 4.3 Moodle 版本演進（依 M.cfg 鍵值與 YUI 版本）
| 存檔 | 特徵 | 判斷 |
|---|---|---|
| 2024-04-14、2024-05-29（themerev 2024-03-07，jsrev 2024-02-23） | 有 `homeurl`、`sessiontimeoutwarning`、`courseId`、`contextInstanceId`，**沒有 `language`**；YUI 3.17.2 | 與 **Moodle 4.0** 鍵值完全一致（4.1 起才有 `language`）【推測】 |
| 2024-07-13 ~ 2025-03-23（themerev 2024-06-24 起） | 多了 `language`；YUI 3.17.2 | **Moodle 4.1–4.3**【推測】（4.4 起 YUI 換成 3.18.1） |
| 2025-11-16 ~ 2026-05（現在 live 也是） | 多了 `apibase`、`siteId`、`userId`；YUI **3.18.1** | **Moodle ≥ 4.5**（4.5 LTS／5.0／5.1 的 M.cfg 相同，無法再細分）【推測】 |

### 4.4 上線時間
- jsrev = **2024-02-23**、boost_union 子修訂 = 2024-02-23、themerev = 2024-03-07；e3.nycu 在 2024-02-26 就已經轉址到 e3p；CDX 首筆 2024-04-14【確認】。
- ⇒ **約 2024-02（112 學年度第 2 學期開學）上線**【推測】。2024-04 以前沒有存檔，所以無法證明更早。

### 4.5 與 e3.nycu 的關係（小結）
- e3p 是**另外建的新 Moodle 站**，不是把 e3.nycu 原地升級：兩台主機同時在線、IP 不同（另見 `04_live_probe.md`）、佈景不同（dcpc vs boost_union）、Moodle 主版本不同（3.8–3.10 vs 4.x）、校外驗證方式不同、單一入口代號不同（newe3 vs newe3p）【確認】。
- 【推測】學校採取「開新站、舊站封存」的作法（而不是把 3.x 直接升級到 4.x），新學期課程開在 e3p，舊學期課程留在 e3.nycu。

---

## 5. 圖片（`/Users/em/Desktop/nctu-e3-history/images/`）

截圖都用全域 `playwright screenshot --full-page --wait-for-timeout 6000~8000` 截取帶工具列的 Wayback URL，截完逐張開啟確認過。

| 檔名 | 內容 | 來源 |
|---|---|---|
| `e3_2006-04_login.png` | 舊 E3 首版登入頁：「國立交通大學網路教學平台 v.3」、e-campus 主視覺、三語切換；最新消息 iframe 當時存到的是 ASP.NET 錯誤頁 | https://web.archive.org/web/20060421232920/http://e3.nctu.edu.tw/NCTU_E3/lms2/login.aspx |
| `e3_2006_copyright.gif` | 舊 E3 版權圖：「版權所有 國立交通大學 Copyright © 2006 National Chiao Tung University」 | https://web.archive.org/web/20060503131837id_/http://e3.nctu.edu.tw:80/NCTU_E3/lms2/Images/Login/zh-TW/copyright.gif |
| `e3_2009-03_login_E3P.png` | `NCTU_E3P` 時期的登入頁：**切圖沒有存檔，只剩框線**，僅用來證明路徑存在 | https://web.archive.org/web/20090301182206/http://e3.nctu.edu.tw/NCTU_E3P/LMS2/login.aspx |
| `e3_2012-06_login_EASY_E3P.png` | `NCTU_EASY_E3P` 時期的登入頁，版面與 2006 相同（拿掉簡體版按鈕） | https://web.archive.org/web/20120615122430/http://e3.nctu.edu.tw/NCTU_EASY_E3P/LMS2/login.aspx? |
| `e3_2007-09_dcpc_portal_home.png` | DCPC 首頁（E3 實際入口），左側 e-Campus 登入框；公告「E2…轉用E3」「e-Campus 3.0 教育訓練」 | https://web.archive.org/web/20070911051426/http://dcpc.nctu.edu.tw/ |
| `e3_2012-01_dcpc_portal_home.png` | 2010 年改版後的 DCPC 首頁，右側藍色 e-Campus 登入框（中下方有 Flash 黑框遮擋） | https://web.archive.org/web/20120101040640/http://dcpc.nctu.edu.tw/ |
| `e3_2016-01_dcpc_portal_home.png` | 2016 年 DCPC 首頁（IE10 相容性設定公告等） | https://web.archive.org/web/20160116021718/http://dcpc.nctu.edu.tw/ |
| `e3_2018-01_dcpc_portal_home.png` | 新舊並行期：「New E3網址 http://e3.nctu.edu.tw/new」公告、「由交大入口網站登入」按鈕 | https://web.archive.org/web/20180113203023/https://dcpc.nctu.edu.tw/ |
| `e3new_2019-07_login.png` | New e3 登入頁（CSS 沒有存到，顯示成無樣式；可看到站名「New e3 數位教學平台」、頁尾 ©2018 數位內容製作中心） | https://web.archive.org/web/20190720040122/https://e3new.nctu.edu.tw/login/index.php |
| `e3new_2020-11_login.png` | New e3 登入頁（完整樣式）：「國立交通大學 數位教學平台」雲朵 logo | https://web.archive.org/web/20201124064122/https://e3new.nctu.edu.tw/login/index.php |
| `logo_e3new_NewE3Cloud_orange_w.png` | New e3 logo 原檔（296×75） | https://web.archive.org/web/20201113132414id_/https://e3new.nctu.edu.tw/pluginfile.php/1/core_admin/logo/0x75/1596591511/NewE3Cloud_orange_w.png |
| `e3nycu_2021-02_login.png` | 合校後的 e3.nycu：「國立陽明交通大學 數位教學平台」、©2021 教學資源組（Wayback 實際給的是 2021-02-13 那份存檔） | https://web.archive.org/web/20210213181123/https://e3.nycu.edu.tw/login/index.php |
| `e3nycu_2022-12_login.png` | e3.nycu 改成校外專用登入＋Google Authenticator 驗證碼欄位、左側「登入說明」 | https://web.archive.org/web/20221222071107/https://e3.nycu.edu.tw/login/index.php |
| `e3p_2024-04_login.png` | e3p 最早的存檔：Email 6 位數驗證碼說明 | https://web.archive.org/web/20240414071219/https://e3p.nycu.edu.tw/login/index.php |
| `e3p_2025-02_login.png` | e3p（Moodle 4.1–4.3 時期） | https://web.archive.org/web/20250212042345/https://e3p.nycu.edu.tw/login/index.php |
| `e3p_2026-05_login.png` | e3p（Moodle ≥4.5 時期；部分 CSS 沒有存到，版面錯位、logo 破圖） | https://web.archive.org/web/20260517184458/https://e3p.nycu.edu.tw/login/index.php |

e3new 2021-01 維護畫面已經有別的筆記存成 `2021-01-28_e3new_maintain.png`（同一張 `maintain.png`），這裡不重複存。

---

## 6. 尚未解決／建議追查
1. **eCampus III 的原始開發者**：DCPC 自述負責「開發與維運」，但 2006 年首版是否委外仍無證據。可以查教務處／DCPC 年報、94–95 學年度教務會議紀錄、或政府電子採購網的「網路教學平台」標案。
2. **舊 E3 停用的正式日期**：只能卡在 2019-09-29 ~ 2020-10-25。New e3 內建的公告（`e3new…/theme/dcpc/news/news_view.php?d=…`）沒有存檔。
3. **2014-09-01 停用的「舊版 e3」**是哪一版：附件 `getFile.aspx?id=61c64dfc-…` 沒有存檔。
4. **e3p 的「p」**、e3.nycu 是否正式定位為「歷史課程封存」：需要教務處教學資源組的公告或會議紀錄。
5. `e3.nctu.edu.tw/new` 的首次啟用：DCPC 公告 2017-09-27，CDX 首筆 2017-11-01。

---

## 附錄 A：舊 E3 `Default.aspx` `<title>` 版本序列（Wayback 時間戳 → title）

```
20060227 NCTU E3 (v1.2006.0224.30796)
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
20090216 eCampus III v1.5.02169.01430   ← 路徑改 NCTU_E3P
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
20100922 eCampus III v1.5.09130.01330   ← 路徑改 NCTU_EASY_E3P
20110702 eCampus III v1.5.06011.01330
20110925 eCampus III v1.5.08241.01330
20111023 eCampus III v1.5.09271.01330
20111106 eCampus III v1.5.10281.00950
20120417 eCampus III v1.5.03262.00936
20120623 eCampus III v1.5.03272.01034
20121104 eCampus III v1.5.09212.01422
20130527 eCampus III v1.5.04103.01000
20140226 eCampus III v1.5.02193.01450   ← 之後到 2016 的 LMS3 都是這一版
```
版號第三段的規則【推測】：v1.1 起是「年尾 1 碼＋月日」（如 `60629` = 2006-06-29）；v1.3 起改成「月日＋年尾 1 碼」（如 `02147` = 02-14-2007，`02193` = 02-19-2013）。

## 附錄 B：Moodle `M.cfg` 鍵值比對表（取自 GitHub `moodle/moodle` 各 STABLE 分支）

| 分支 | 鍵 |
|---|---|
| 3.2 | wwwroot sesskey themerev slasharguments theme jsrev admin svgicons contextid |
| 3.3–3.7 | ＋ iconsystemmodule usertimezone |
| 3.8–3.10 | ＋ sessiontimeout langrev templaterev |
| 3.11 | ＋ sessiontimeoutwarning |
| 4.0 | ＋ homeurl courseId courseContextId contextInstanceId |
| 4.1–4.3 | ＋ language |
| 4.4 | ＋ siteId（YUI 3.18.1） |
| 4.5／5.0／5.1 | ＋ apibase userId（YUI 3.18.1） |

## 附錄 C：工作檔（scratchpad，暫存）
- 自己重抓的 CDX：`/private/tmp/claude-501/-Users-em-Desktop/ef64c714-0ca3-493b-bc59-04ddbcca6a4f/scratchpad/e3hist_cdx/`（共用 `dl/` 目錄的 CDX 檔在調查途中被其他程序覆寫，所以另外重抓了一份）
- 抓下的原始頁面：`/private/tmp/claude-501/-Users-em-Desktop/ef64c714-0ca3-493b-bc59-04ddbcca6a4f/scratchpad/pages/`
