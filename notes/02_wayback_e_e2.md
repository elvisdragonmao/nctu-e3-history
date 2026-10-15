# 02 — 早期世代：e.nctu.edu.tw（E.NCTU 交大網路校園）與 e2.nctu.edu.tw（eCampus）

> 資料來源：Internet Archive Wayback Machine（CDX 索引＋`id_` 原始存檔）。2026-10-16 查詢。
> 標記說明：**〔原文〕** 為存檔頁面原文摘錄；**〔推測〕** 為依時間點或旁證推論，未見直接文字證據。
> Wayback 連結格式：`https://web.archive.org/web/<timestamp>/<url>`。

---

## 0. 一句話結論

- **e.nctu.edu.tw = 「E.NCTU 交大網路校園」**：2000 年由交大「網路大學推動小組」／理學院「網路學習研究中心」自行開發的 eLearning 平台（FreeBSD + PostgreSQL + PHP，討論區用 Phorum 3.2.11）。2000-11-04 V1.0 全面開放測試，2001–2002 為全校網路教學平台；2002-10 起功能縮減，最後一筆完整存檔 2004-02-12。
- **e2.nctu.edu.tw = 「eCampus」**：2002 年 9 月上線的 ASP.NET 平台（登入頁標題「eCampus Login Page」，後為「登入 eCampus 系統 (版本號)」），由教務處網路教務組推廣，校方稱「e-campus」。最後版本號 4.0.2005.0217。DCPC 公告 **2007 年 9 月底停止服務**、請教師轉用 e3（伺服器頁面在存檔中延續到 2009 年）。
- **e3 = eCampus III（DCPC 稱「e-Campus 3.0」）**：2006-02 起出現在 `e3.nctu.edu.tw/NCTU_E3/lms2/`；**2006-05 起 e.nctu.edu.tw 根目錄 302 轉到 `/NCTU_E3/lms2/Default.aspx`**（也就是舊 E.NCTU 網域被拿來掛 E3）；2007-12 起 e.nctu.edu.tw 再改轉到數位內容製作中心 dcpc.nctu.edu.tw。
- 2006–2007 年 e2 和 e3 **同時並存**（校方「NCTU 線上學習」頁同時列 e3、e2、BlackBoard 三個平台）。**交接公告在數位內容製作中心（DCPC）首頁，不在 e2 本身**：DCPC 2007-08-16 最新消息「**E2網路教學平台提供服務至九月底止，請教師們轉用E3平台**」，內文說 e3（「網路教學平台e-Campus（簡稱e3)」）「已正式上線一年」、「目前已有166位教師選用」。e2 登入頁存檔沒有這則公告；e3 早期登入頁也沒有沿革說明（只有「版權所有 國立交通大學 Copyright © 2006」圖片）。DCPC 同期另一則消息稱 E3 為「**e-Campus 3.0** 網路教學平台」。

---

## 1. 時間軸

| 日期 | 事件 | 證據 |
|---|---|---|
| 民國 83 年（1994）起 | 孫春在、周倩教授研究群開始遠距教學研究 | Profile.htm〔原文〕 |
| 民國 87 年（1998） | 理學院林松山院長整合資源建構「網路高中數學學習館」（informath.nctu.edu.tw），隨後成立「網路學習研究中心」 | Profile.htm〔原文〕 |
| 2000-06（民國 89 年 6 月） | 「網路大學推動小組」成立，魏副校長任召集人、陳明璋博士任執行秘書；教務處成立「網路教務組」 | Profile.htm〔原文〕；dcpc aboutus_01.htm |
| 2000-07 | E.NCTU 系統開始開發（初期 3 名軟體工程師，9 月後擴編到 11 人） | Profile.htm〔原文〕 |
| 2000-10-17 | 「第一次網路教材設計實務研習會」，介紹「已開發完成一套網路教學平台 E.NCTU，即將開放全校師生使用」 | news/news-1017.htm |
| 2000-10-24 | 系統停機公告 | index_new.htm（2000-12） |
| **2000-11-04** | **「交大網路校園 V1.0」全面開放測試** | index_new.htm（2000-12） |
| 2000-11-11 ~ 11-13 | 廣告稿出爐、公開說明會開放報名、「E.NCTU 網路校園公開命名」開始 | 同上 |
| 2000-11-23 | 新增組織群組「E.NCTU 園地」「各系級組織列表」 | 同上 |
| 2000-12-06 | Wayback 第一筆 e.nctu.edu.tw 存檔（index_new.htm） | CDX |
| 2000-12-20 | 公開命名活動中獎名單 | index_new.htm（2001-02） |
| 2000-12-29 | 「2000 網路學習理論與實務研討會」（浩然地下室） | 同上 |
| 2001-04 | 首頁改版（`HTML/Index/200104/` 新版切圖），根目錄 refresh 到 index_new.htm | CDX／首頁原始碼 |
| 2001-04-29 | 停機做資料庫系統升級及檔案伺服器調整 | news/news20010425.htm |
| 2001-05 | 網路學習研究中心預計遷入科學一館 307、304 室 | news/news20010419.htm |
| 2001-06 | 根目錄改 refresh 到 `index_new.php`（動態首頁，含「E.NCTU 人氣排行榜」） | CDX：root digest 於 2001-06-28 改變 |
| 2001-09 | 網路教務組發行《網路教學教師手冊（E.NCTU）》（90.09） | 網路教務組 old news |
| 2002-01 ~ 2003-08 | www.nctu.edu.tw 首頁直接連「網路大學 e.nctu」 | www 首頁存檔 |
| 2002-03-15 | E.NCTU 公告登入方式：帳號＝學號／教職員代號、密碼＝身分證後六碼 | Board/news/query2.php?id=19 |
| **2002-09-14** | **e2 eCampus 最早一則最新消息「新手請看下方之相關連結」** | e2 eCampus/default.aspx（2002-10） |
| 2002-09-23 | e2：「本校師生請使用選課系統帳號/密碼登入本系統」 | 同上 |
| **2002-10-10** | **Wayback 第一筆 e2.nctu.edu.tw 存檔**；根目錄 302 → `http://140.113.8.88/eCampus/default.aspx` | CDX／HTTP header |
| 2002-10-15 | E.NCTU：遭人擺放 mp3，接獲 IFPI 通知，要求刪除違法檔案 | query2.php?id=21 |
| 2002-10-18 / 10-22 | E.NCTU 個人資料夾上傳功能移除；個人資料夾 11/1 移除 | query2.php?id=22、23 |
| 2003-02-25 | E.NCTU 最後一則公告（科管所推廣教育碩士學分班登入方法） | query2.php?id=24 |
| 2003-06 | e2 登入頁顯示版本「eCampus 系統 (2.0.0.312)」 | e2 存檔 2003-06-04 |
| 2003-08 | e2 版本「2.2.0.0613」 | e2 存檔 2003-08-15 |
| 2003-09 ~ 2005 | 「NCTU 線上學習」頁出現（HTM/online-index.htm 最早存檔 2003-09-06，內容仍列「e.nctu網路校園」）；2004-07 起確認校首頁改連此頁；2005-02 版改列 e2 與 bb | online-content.htm／online-index.htm／www 首頁 2004-07 |
| 2003-11 ~ 2004-06 | e2 default.aspx 只回傳「本系統必須使用 IE 6.0（含）以上版本…」（存檔爬蟲非 IE 所致） | e2 存檔 2003-11-01 |
| 2004-02-12 | E.NCTU 最後一批 200 存檔（Profile.htm、teamgroup 等） | CDX |
| 2004-03-10 | 網路教務組「網路教學工作坊(二)」：介紹「e-campus 討論區」，「e-campus 網址：http://e2.nctu.edu.tw」 | ~nacad/news/news.htm |
| 2004 | e2 另掛「台灣聯合大學網路教學課程 選課登錄系統」（course.asp，四校學生選修交大全網路課程） | e2 Course/course.asp |
| 2006-02-27 | Wayback 第一筆 e3.nctu.edu.tw（`/NCTU_E3/lms2/Default.aspx`） | e3 CDX |
| 2006-04 | e2 版本「4.0.2005.0217」；最新消息 2006/03/06「學生看不到課程資料問題」 | e2 存檔 2006-04-23 |
| 2006-04 | 「NCTU 線上學習」頁同時列 bb、e2、e3 | ~nacad/nctu_online/ 2006-04-22 |
| **2006-05-20** | **e.nctu.edu.tw 根目錄 302 → `/NCTU_E3/lms2/Default.aspx`（eCampus III）** | HTTP header |
| 2006（民國 95 年） | 網路教務組與交大出版社合併為「數位內容製作中心」(DCPC) | dcpc aboutus_01.htm |
| 2006-11 | 經 e.nctu.edu.tw 存到的 E3 頁標題「eCampus III v1.2.61103.00219」 | e.nctu.edu.tw/NCTU_E3/lms2/Default.aspx |
| 2006-12 ~ 2007-09 | e2 另掛 `/fsreg/` 外籍生線上申請系統（Foreign Student On-Line Application System） | e2 CDX |
| 2007-02 | www.nctu.edu.tw/campus/index.html（校園資訊）仍有「交大網路校園」→ e.nctu.edu.tw | campus 存檔 |
| 2007-03 | 「NCTU 線上學習」頁：e3網路教學平台、e2網路教學平台、BlackBoard網路教學平台 | ~nacad/nctu_online/ 2007-03-08 |
| **2007-08-16** | **DCPC 公告「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」**；e3「已正式上線一年」、166 位教師使用 | dcpc.nctu.edu.tw 首頁＋popup.aspx（存檔 2007-09-11／09-17） |
| 2007-08-30 | DCPC：「9月6日【e-Campus 3.0 網路教學平台教育訓練課程】」 | dcpc 首頁 2007-09-11 |
| 2007-09-07 | DCPC：「e3同步、e3同步上線了！敬請各位上e3網路教學平台一探究竟」 | 同上 |
| **2007-09-30** | **〔依公告〕e2 停止服務**（實際上伺服器頁面到 2009 年仍可存取，見下） | 同上 |
| **2007-12-15** | **e.nctu.edu.tw 根目錄改 302 → dcpc.nctu.edu.tw**（2008-11 甚至直接以 200 回應 DCPC 首頁） | HTTP header |
| 2008-08 | www.nctu.edu.tw 首頁直接列「BB教學平台」「e3教學平台」，不再列 e2 | www 首頁存檔 |
| 2009-02 | campus/index.html 已移除「交大網路校園」連結 | campus 存檔 |
| 2009-03-31 | e2 登入頁最後一筆 200 存檔（內容與 2008-01 相同，無最新消息） | e2 CDX |
| 2009-07-29 | e2 `ECAMPUS_HELP` 說明頁最後一筆 200 存檔 | e2 CDX |
| 2021-04-12 | e2.nctu.edu.tw 根目錄 302 → https://dcpc.nctu.edu.tw/index.aspx | HTTP header |

e2 的正式停止服務日期依 DCPC 2007-08-16 公告為 **2007 年 9 月底**。〔推測〕之後伺服器沒有立即關閉：登入頁 2008-01 ~ 2009-03 仍回應 200（但「沒有最新消息」），ECAMPUS_HELP 2009-07 仍可存取；可能保留給舊課程查閱。

---

## 2. e.nctu.edu.tw —「E.NCTU 交大網路校園」

### 2.1 基本資料

| 項目 | 內容 |
|---|---|
| 系統名稱 | E.NCTU／e.nctu 網路校園／交通大學網路校園（首頁 `<title>`：「交通大學網路校園」→「E.NCTU首頁」） |
| 定位 | 「eLearning 建構平台及內容提供（eLearning Platform & Content Provider）」 |
| 開發單位 | 交大「網路大學推動小組」；系統平台由理學院「網路學習研究中心」（頁尾作「網路學習研發中心」）開發 |
| 主管／召集 | 魏副校長（召集人）、陳明璋博士（執行秘書）、教務長蔡文祥、理學院院長林松山 |
| 技術 | **FreeBSD + PostgreSQL + PHP**；伺服器端以 Open Source 為主；首頁用 Macromedia Fireworks 切圖（meta「Fireworks Splice HTML」）；討論區 **Phorum 3.2.11**（meta `Phorum Version 3.2.11`、`Phorum DB postgresql65`）；說明文件用 MS Word 存 HTML |
| 用戶端 | 「請使用 Internet Explorer 4.0 以上的瀏覽器」；建議 Pentium III、64M RAM、1024×768 |
| 版權宣告 | 2000：「Copyright 2000 網路學習研究中心Inc. All rights reserved.」；2001–2003：「Copy Right 1999~2001 by The NCTU Network University Work Group. All Right Reserved. E.NCTU 乃國立交通大學理學院 網路學習研發中心 版權所有」 |
| 聯絡 | 2001：網路大學推動小組，科學一館 229、231 室，ext 56407、56438，Help@E.NCTU.edu.tw；2003 版 Profile：網路學習研究中心，科學一館 307 室，ext 56053，Fax 03-5734448；客服專線 56053（週一至五 8:30–17:30、週六 8:30–12:00） |
| 帳號 | 「通行帳號／隨身密碼／認證碼」；2002 起帳號＝學號或教職員代號、密碼＝身分證後六碼；每人 10MB 個人工作室網頁空間 |

### 2.2 功能

依「關於本站」與「網站導覽」(property/service/system/map.php)：

- **個人工作室**：小秘書（作業狀況）、個人資料、我的組織列表、查詢使用者、我的書籤、個人通訊錄、答錄機、行事曆、記事本、聊天室、環境設定、意見信箱、資料夾。
- **組織建館**（課程、行政單位、研究單位、教學單位、社團都是「組織」）：組織管理首頁、**資源（教材）管理**、**檔案管理**、**課業管理（新增作業、繳交作業、改作業及給分）**、組織成員管理、組織行事曆、**討論區（Phorum）**、共用通訊錄、公告欄、教學活動管理。
- **使用者介面**：申請帳號、忘了密碼、常見問題、系統說明、校園守則、救援大隊（客服）、相關連結、工作團隊、資訊廣場、內容搜尋。
- **系統管理**：系統管理者（帳號、組織、看板）、組織管理者（成員）。
- 「藍色小精靈」線上說明助手（2001-09 公告可自行關閉）。

所以使用者說「當時好像只有教材管理」不完全正確：教材管理（資源管理＋檔案管理）是核心，但 2001 年就已經有作業繳交、討論區、行事曆、公告欄等功能（Profile 原文說「在 V2.0 版時更有『繳交作業』及『管理統計』等功能」）。

組織列表（org/orglist.php，2001-06）頂層分類：89年度第一學期課程、89年度第二學期課程、E.NCTU 園地、各系級組織列表、行政單位、研究單位、教學單位、學生社團。

### 2.3 統計

- 2001-06-18「E.NCTU 人氣排行榜」（組織人次）：1 法老研習社 185、2 線性代數 143、3 計算機概論(二) 121、4 作業系統 71、5「資訊行為」網路教室 58、6 離散數學 53、7 計算機導論（二）51、8 中國傳統政治 45、9 寬頻無線行動通信系統 33、10 圖書館學概論 33。
- Phorum 討論區範例：「慢性疾病成因預防及醫學網路(6661)討論區」文章 130 篇（2002-06 存檔）；「Java程式設計 (1099)討論區」（2002-04）。
- 開發團隊規模：Profile 原文說「從當時兩三人的研究團隊，發展到現在有 11 人規模的專案型組織」。
- **沒有找到**全站帳號數或課程總數的統計。

### 2.4 重要頁面摘錄

**關於本站 Profile.htm**（「網路大學推動小組 2000年獻禮」）
- 2001-03 版：https://web.archive.org/web/20010302091059/http://e.nctu.edu.tw/news/Profile.htm
- 使用者找到的 2003-12 版：https://web.archive.org/web/20031204104846/http://e.nctu.edu.tw/news/Profile.htm （正文與 2001 版相同，只有「如何連絡我們」改成網路學習研究中心／科學一館 307）

> 〔原文〕「E.NCTU(網址為e.nctu.edu.tw)是『網路學習研究中心』所建構的第二個網站。（第一個是數學學習館，網址為informath.nctu.edu.tw。）」
> 〔原文〕「E.NCTU的服務對象，鎖定在國立交通大學…的教職員、學生、社團及校友。」
> 〔原文〕「交通大學『網路大學推動小組』於民國89年6月成立，由魏副校長擔任召集人、陳明璋博士擔任執行秘書…在教務處成立『網路教務組』負責處理網路大學教務工作，理學院林院長領導的『網路學習研究中心』負責網路教學的系統平台之發展與應用」
> 〔原文〕「自2000年07月至今，E.NCTU系統發展的時間相當短…從當時兩三人的研究團隊，發展到現在有11人規模的專案型組織。」
> 〔原文〕「以課程這種組織為例，老師可以利用MicroSoft Office編輯教材，另存新檔產生的HTML，或善用FrontPage、Java、Flash等…來編輯動態教材，上傳到『檔案管理』，利用『資源(教材)管理』進行課程編排及分類，供學生點選上課。在V2.0版時更有『繳交作業』及『管理統計』等功能。」
> 〔原文〕「整個E.NCTU系統，在Server端均以Open Source Solution 之軟體為採用重點…FreeBSD (O.S.) ＋PostgreSQL（DataBase） ＋PHP (Programming Tool)」
> 〔原文〕展望：「希望能逐步成為學界eLearning通用平台的提供者，並朝『多校別集中管理』、『各校分散發展應用』的目標」

**首頁 index_new.htm（2000-12，V1.0 時期）**：https://web.archive.org/web/20001206215100/http://e.nctu.edu.tw/index_new.htm
> 〔原文〕最新消息：「交大網路校園V1.0" 全面開放測試 (11/04)」「E.NCTU網路校園公開命名正式開始 (11/13)」「交大網路校園公開說明會 (11/12)」「〝第一次網路教材設計實務研習會〞歡迎蒞臨參觀指教 (10/17)」

**首頁 index_new.php（2001-06）**：https://web.archive.org/web/20010619061708/http://e.nctu.edu.tw/index_new.php
> 〔原文〕「E.NCTU人氣排行榜出爐囉!」「停機公告--2001/04/29(日)」「『網路學習研究中心』是怎麼來的?? 現在在那裡??」「九十年度教育部補助專科以上學校開辦遠距教學課程」「理學院網路學習碩士專班」；頁尾 banner 連到倪匡科幻獎、理學院網路學習碩士專班、交大首頁、科學學習館 inforscience、台灣網路大學系統 informath.nctu.edu.tw/twnua。

**首頁 index_new.php（2003-12，最後版本）**：https://web.archive.org/web/20031203233453/http://e.nctu.edu.tw/index_new.php
> 〔原文〕只剩兩則公告：「2003-02-25 九十一學年度第二學期科技管理研究所推廣教育碩士學分班-學生登入方法」「2002-03-15 關於登入的方法」

**最新消息（Board/news/query2.php?id=N）**
- id=19（2002-03-15）https://web.archive.org/web/20021231102242/http://e.nctu.edu.tw/Board/news/query2.php?id=19
  > 〔原文〕「通行帳號:學號或教職員代號／通行密碼:身分證字號後六碼(僑生為護照後六碼)／若無法登入，請聯絡網路教務組(50151~3)」
- id=21（2002-10-15）https://web.archive.org/web/20021231101541/http://e.nctu.edu.tw/Board/news/query2.php?id=21
  > 〔原文〕「經查e.nctu遭不明人士擺放mp3供人下載，已獲IFPI通知將相關檔案刪除。…近期內本系統將做全面性的檔案普查」
- id=22（2002-10-18）https://web.archive.org/web/20021231101129/http://e.nctu.edu.tw/Board/news/query2.php?id=22
  > 〔原文〕「個人資料夾-上傳功能：此功能已奉今移除, 請勿再詢問相關問題.」
- id=23（2002-10-22）https://web.archive.org/web/20021231102953/http://e.nctu.edu.tw/Board/news/query2.php?id=23
  > 〔原文〕「請將個人資料夾中的檔案清除, 此功能將於11月1日移除.」
- id=13（2001-09-10）小精靈說明；id=15（2001-09-27）請學生登錄 e-mail。

〔推測〕2002-10 的 mp3／IFPI 事件、個人資料夾移除，和 e2（eCampus）2002-09 上線同一時間。E.NCTU 之後只剩推廣教育學分班使用，看起來在 2002 學年度起被 e2 取代為全校主要平台。

**網路學習研究中心是怎麼來的（news20010419.htm）**：https://web.archive.org/web/20010615002334/http://e.nctu.edu.tw/news/news20010419.htm
> 〔原文〕「E.nctu，是『網路學習研究中心』所發展的網站系統…目前由交通大學理學院林松山院長的支持，在理學院科學一館撥出三樓307及304室共約有20坪辦公空間…預計在2001年5月份遷入。」

**第一次網路教材設計實務研習會（news-1017.htm）**：https://web.archive.org/web/20010309020357/http://e.nctu.edu.tw/news/news-1017.htm
> 〔原文〕「本校已成立『網路教務組』且本『網路學習研究中心』已開發完成一套網路教學平台E.NCTU，即將開放全校師生使用。」時間：八十九年十月十七日；主辦：教務處網路教務組、網路學習研究中心；主持人：蔡文祥教務長、林松山院長。

**工作團隊（teamgroup/index.htm）**
- 2001-05：https://web.archive.org/web/20010501180540/http://e.nctu.edu.tw/teamgroup/index.htm
- 2004-02：https://web.archive.org/web/20040212014131/http://e.nctu.edu.tw/teamgroup/index.htm
> 〔原文〕「本網站是由交通大學網路大學相關計劃所支持，系統設計由交通大學網路學習研發中心所負責設計。」
> 2001 成員：執行秘書 陳明璋；專案管理 施蔚芝、李俊佳；行政企劃 王東濬、呂英蕙、柯柏成；內容編輯 陳超然；系統發展 馮寶永、林翔；系統維護 林俊良、陳撲賢；美術編輯 涂曉倩（e-mail 都在 @InForMath.NCTU.edu.tw）。
> 2004 成員：執行秘書 陳明璋；專案管理 李俊佳；行政企劃 柯柏成、呂英蕙；系統發展 馮寶永；系統維護 劉法強、陳撲賢；美術編輯 涂曉倩。

**網路校園守則（rules/rules.php）**：https://web.archive.org/web/20010303033803/http://e.nctu.edu.tw/rules/rules.php
> 〔原文〕「歡迎您加入e.nctu 網路校園, 本站之服務保證讓會員﹕1. 人人有10MB之個人工作室網頁。2. 各課程、各部門、各社團均可申請組織…」

**操作手冊／系統說明（Manual/index.htm → Doc/HTML/E.NCTU系統說明文件--Content.htm）**
- https://web.archive.org/web/20010301212539/http://e.nctu.edu.tw/Manual/index.htm
- 目錄存檔 2001-03-09：https://web.archive.org/web/20010309215015/http://e.nctu.edu.tw/Doc/HTML/E.NCTU%A8t%B2%CE%BB%A1%A9%FA%A4%E5%A5%F3--Content.htm
> 「E.NCTU 系統說明文件」章節：申請帳號（教職員正式／約雇、學生、校外人士）、登錄「E.NCTU」、進入「組織建館」、師生互動環境簡介、個人工作室各功能、組織建館、資源管理（新增 link／目錄／從檔案庫新增／編輯「開放、隱藏、分享」／資源芳鄰）、檔案管理（上傳、解壓、寄給好友…）、申請擴大網頁空間、**課業管理—新增作業、繳交作業、改作業及給分**、公告欄、組織行事曆、共用通訊錄、組織管理篇。另提供 DOC.zip 下載。

**FAQ（Doc/FAQ/常見問題.htm）**：https://web.archive.org/web/20010303194228/http://e.nctu.edu.tw/Doc/FAQ/%B1%60%A8%A3%B0%DD%C3D.htm
> 問題清單：申請帳號時資料與校方不符、能不能改「隨身密碼」、何謂通行帳號／隨身密碼／認證碼、在家或校外使用的狀況、有沒有測試帳號、有 Error Message 系統好像有 BUG、為什麼這個組織空空的沒有管理者卻有人氣、檔案管理解壓縮不成功又說空間已滿。後期 FAQ 改成 frameset 嵌入 `property/service/qa/query1.php`（2001 年版指向 `infopc09.math.nctu.edu.tw`）。

**Phorum 討論區**：https://web.archive.org/web/20020425075307/http://e.nctu.edu.tw/bbs/list.php?f=1271&t=1&a=1 （Java程式設計 (1099)討論區，2002-04）

### 2.5 e.nctu.edu.tw 之後的轉址

| 存檔時間 | 根目錄回應 |
|---|---|
| 2001-04 | 200，meta refresh → `index_new.htm` |
| 2001-06-28 ~ 2003-12-03 | 200，meta refresh → `index_new.php` |
| 2004-02-12 | 最後一批內容頁 200 |
| 2004-02 ~ 2006-02 | 無根目錄存檔；2006-02-20 `/Plaza/` 已 404 |
| **2006-05-20 ~ 2007-08-30** | **302 → `http://e.nctu.edu.tw/NCTU_E3/lms2/Default.aspx`**（E3／eCampus III 用同一台主機或同一個名稱掛載；2006-11 有大量 `e.nctu.edu.tw/NCTU_E3/lms2/stu_*.aspx` 存檔） |
| **2007-12-15 ~ 2012** | **302 → `http://dcpc.nctu.edu.tw/`**（數位內容製作中心） |
| 2023 | 變成客家文化學院網站（`/zh_tw/News/...`），和本研究無關 |

另：`e.nctu.edu.tw/NCTU_E3P/LMS2/Default.aspx` 在 2009-02-28 有一筆存檔（E3P）。

---

## 3. e2.nctu.edu.tw —「eCampus」（校方稱 e-campus）

### 3.1 基本資料

| 項目 | 內容 |
|---|---|
| 系統名稱 | eCampus（登入頁 `<title>eCampus Login Page</title>`；2003 起「登入 eCampus 系統 (版本)」；logo 圖為「ecampus」字樣）；網路教務組文件稱「e-campus」；2007 年「NCTU 線上學習」頁稱「e2網路教學平台」 |
| 主機 | 2002–2003 根目錄 302 到 IP `140.113.8.88/eCampus/default.aspx`；2005 起轉 `e2.nctu.edu.tw/eCampus/default.aspx` |
| 技術 | **ASP.NET（C#）**：meta `GENERATOR = Microsoft Visual Studio 7.0`、`CODE_LANGUAGE = C#`；頁面為 `.aspx`；**限 IE 6.0 以上**；上傳檔案需安裝 ActiveX「**GxWebFtp ActiveX Control**」；登入影片教學 `.wmv`。另有傳統 ASP 頁面 `Course/course.asp`、`CourseSignUp/course.asp` |
| 版本號 | 2003-06：2.0.0.312；2003-08：2.2.0.0613；2006-04 ~ 2009：4.0.2005.0217 |
| 登入身分 | 2002：「請先選身份：系統管理員／教師／學生」；2003 中改成不選身份 |
| 帳號 | 「本校師生請使用選課系統帳號/密碼登入本系統」（2002-09-23） |
| 訪客功能 | 最新消息、**火線討論區**（2002-10 版有，2002-12 版已拿掉）、相關連結、客服專區／服務台專區 |
| 營運／推廣單位 | 教務處**網路教務組**（nacad@cc.nctu.edu.tw）→ 2006 年起為**數位內容製作中心**（DCPC） |
| 開發廠商 | **存檔中找不到**。頁面上沒有版權文字（logo 圖只有「ecampus」與「國立交通大學」校徽圖） |
| 版權宣告 | 登入頁上沒有文字版權宣告 |
| 統計 | 沒有找到使用人數或課程數；`sys_utiltiy_getonlinecount.aspx`（線上人數）存檔都被 302 導回登入頁 |

〔推測〕E3 頁面標題是「eCampus III」、DCPC 稱「e-Campus 3.0」並說「網路教學平台e-Campus（簡稱e3)」，e2 的系統叫「eCampus」。命名上 e → e2 → e3 對應第一、二、三代平台，e2 看起來是 eCampus 第二代；但 e2 頁面上從來沒出現「eCampus II」字樣，版本號也是 2.x → 4.0，兩者是否同一套程式碼／同一廠商，存檔無法證實。

### 3.2 功能（從頁面與說明文件可見）

- 講義、作業、測驗、討論、參考資料上傳（教師）；作業、討論上傳（學生）——ECAMPUS_HELP「安裝上傳作業元件」原文：「需要使用此元件的功能：1. 教師 - 講義, 作業, 測驗, 討論, 參考資料 2. 學生 - 作業, 討論」。
- 學生端頁面名稱（2006 存檔 URL）：`stu_main_frame`、`stu_crsview_frame`、`stu_crsview_news_list`（課程公告）、`stu_discuss_topic_index/view`（討論區）；教師端 `tea_discuss_topic_reply`。
- 網路教務組 2004-03 工作坊介紹「e-campus 討論區的介紹與使用技巧」。
- DCPC 2007-10「教學平台介紹」描述的 e-campus 功能（〔推測〕這段可能已經是在講 E3／eCampus III，因為當時 E3 已上線）：〔原文〕「e-campus 為本校目前所使用的網路教學平台，提供了在網路上存取教材、進行溝通討論、問卷和測驗、繳交與批閱作業、管理成績和學習追蹤等多項功能…可隨時切換三種語系（繁體中文、英文、簡體中文）…有課程旁聽功能、訪客參觀功能…」

### 3.3 e2 主機上的其他系統

- **台灣聯合大學網路教學課程 選課登錄系統**（`Course/course.asp`，2004）
  https://web.archive.org/web/20040907042736/http://e2.nctu.edu.tw/Course/course.asp
  > 〔原文〕「本系統為四校學生登錄選修網路教學課程而設立,請在各校選修交通大學所開之完全網路教學課程,並請在此登錄系統上,輸入個人相關資訊,以利於網路學習平台上建立使用帳號」
  > 2004-09 課程：6123 網路文學（劉龍勳）、6314 全球化與兩岸關係（劉河北）、6646 網路與社會（孫治本）、6534 網路社會導論（楊永良等）、6601 印象派及其時代（王美鴻等）、6602 計算機科技新知（李明山）、6556 人體生化營養學。
- 2003-02 `CourseSignUp/*.htm` 課程介紹（例如 6123 網路文學課綱，成績含「線上討論 30%」）。
- 2006-12 ~ 2007-09 `/fsreg/`：「Welcome to NCTU:::Foreign Student On-Line Application System」（外籍生申請，和教學平台無關）。
- 2009-04 `/ltrc` 403（語言教學與研究中心）。

### 3.4 重要頁面摘錄

**登入首頁 2002-10（最早）**：https://web.archive.org/web/20021010082927/http://e2.nctu.edu.tw/eCampus/default.aspx
> 〔原文〕最新消息「2002/09/14：新手請看下方之相關連結　2002/09/23：本校師生請使用選課系統帳號/密碼登入本系統.　2002/09/24：系統更新說明」
> 火線討論區：「2002/10/08：Re:非ie的瀏覽器」「Re:網路社會導論 是要去哪裡po文章ㄚ」「Re:About中國傳統政治...」
> 相關連結「觀看此平台登入/登出介紹」（SystemHelp/01登入登出v7.wmv）

**最新消息列表 2002-12**：https://web.archive.org/web/20021210043226/http://e2.nctu.edu.tw/eCampus_GuestView/sys_new_view.aspx
> 〔原文〕「本校師生請使用選課系統帳號/密碼登入本系統. 2002/9/23 上午 10:28:59」「新手請看下方之相關連結 2002/9/14 下午 07:36:48」

**登入頁 2003-01**（新增「2002/12/25：上傳元件(ActiveX control)下載問題」）：https://web.archive.org/web/20030109212507/http://e2.nctu.edu.tw/eCampus/

**登入頁 2003-08（版本 2.2.0.0613）**：https://web.archive.org/web/20030815230004/http://e2.nctu.edu.tw/eCampus/default.aspx

**登入頁 2006-04（版本 4.0.2005.0217）**：https://web.archive.org/web/20060423035328/http://e2.nctu.edu.tw/ecampus/default.aspx
> 〔原文〕最新消息「2006/03/06：學生看不到課程資料問題」「2005/09/16： IE設定(重要)」；相關連結含「上傳作業元件安裝設定」（E2.NCTU.EDU.TW/ECAMPUS_HELP/安裝上傳作業元件.htm）。

**登入頁 2008-01 ~ 2009-03（最後）**：https://web.archive.org/web/20090331063829/http://e2.nctu.edu.tw/eCampus/default.aspx
> 「最新消息：沒有最新消息...」——**沒有**任何「請改用 e3」的公告。

**操作說明**
- e-campus 系統使用說明（學生版，frameset banner_s.htm + get_started.htm）：https://web.archive.org/web/20060423035228/http://e2.nctu.edu.tw/eCampus_Help/student/index.htm
- 設定快顯封鎖程式（2005-06）：https://web.archive.org/web/20050617033051/http://e2.nctu.edu.tw/ECAMPUS_HELP/%E8%A8%AD%E5%AE%9A%E5%BF%AB%E9%A1%AF%E5%B0%81%E9%8E%96%E7%A8%8B%E5%BC%8F.htm
  > 〔原文〕「方法一：允許 eCampus 網站的快顯功能…在『要允許的網站位址』中輸入 http://e2.nctu.edu.tw/」
- 安裝上傳作業元件（2007-12）：https://web.archive.org/web/20071204193910/http://e2.nctu.edu.tw/ECAMPUS_HELP/%E5%AE%89%E8%A3%9D%E4%B8%8A%E5%82%B3%E4%BD%9C%E6%A5%AD%E5%85%83%E4%BB%B6.htm
  > 〔原文〕「安裝上傳元件『GxWebFtp ActiveX Control』…第一次於本系統任一可上傳檔案的頁面會跳如圖所示的對話方塊, 請選擇『是(Y)』安裝該元件即可」
- FAQ（GuestView/cus_faq_list.aspx）：**沒有存檔**。

**網路教務組公告（2004-03）**：https://web.archive.org/web/20040308110113/http://www.cc.nctu.edu.tw/~nacad/news/news.htm
> 〔原文〕「網路教學工作坊(二)：線上討論區的活動設計與經營…2. e-campus 討論區的介紹與使用技巧，本校通識中心王美鴻老師主講　時間：九十三年三月十日(三)…e-campus 網址：http://e2.nctu.edu.tw」
> 舊消息（old news）還列著「網路教學教師手冊( E.NCTU ) 90.09」「鼓勵開設網路教學課程辦法 92.05.13」「ISO9001-2000版 網路教學規劃作業程序 92.06.17」。

---

## 4. e、e2、e3 的關係與交接

1. **E.NCTU（e）**：2000-11 V1.0，2001–2002 學年為全校網路教學平台（自行開發、PHP）。開發者是理學院網路學習研究中心；教務處網路教務組負責教務與推廣。
2. **eCampus（e2）**：2002-09 上線（91 學年度第一學期），由網路教務組推廣，帳號改用選課系統帳號。同一時間 E.NCTU 移除個人資料夾等功能。〔推測〕這時 e2 取代 e 成為主要平台，e 只剩零星課程（2003-02 推廣教育學分班）使用，2004 年後停止更新。
3. **eCampus III／e-Campus 3.0（e3）**：2006-02 起出現在 e3.nctu.edu.tw（DCPC 2007-08 公告說「已正式上線一年」，〔推測〕正式啟用約 2006 年 8–9 月、95 學年度第一學期）；**2006-05 起舊網域 e.nctu.edu.tw 直接轉址到 E3**。2006–2007 年 e2 與 e3 並存（也和 BlackBoard bb.nctu.edu.tw 並存，bb 在 2005-02 已列在「NCTU 線上學習」）。2008-08 校首頁只列 BB 與 e3，e2 不再出現在校首頁。
4. **交接公告**：e2 登入頁（2006-04 ~ 2009-03 存檔）本身沒有「改用 e3」公告；公告發在 DCPC 首頁——2007-08-16「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」，popup 內文：〔原文〕「本校網路教學平台e2提供服務至九月底止，請教師們提早轉用e3平台。教師在轉換平台時如有任何使用疑問，歡迎洽詢數位內容製作中心陳小姐（校內分機31433），並可提供個別的使用之教育訓練，或協助將教材轉移到新的網路教學平台e3。網路教學平台e-Campus（簡稱e3)：目前已有166位教師選用的e3網路教學平台，已正式上線一年，系統更穩定、功能更強大，且介面更親和美觀。」來源：https://web.archive.org/web/20070911/http://dcpc.nctu.edu.tw/ （首頁）、https://web.archive.org/web/20070917181422/http://dcpc.nctu.edu.tw/popup.aspx?type=1&id=3e3137da-d804-4c49-a4aa-4ebde347c987 （內文；action.aspx 會 302 到這頁）。**e3 早期登入頁沒有沿革說明**（2006-04、2006-11 登入頁只有圖片切版、login_news iframe、「版權所有 國立交通大學 Copyright © 2006 National Chiao Tung University」圖片）。
5. 營運單位沿革（DCPC「關於我們」2007-09）：〔原文〕「國立交通大學在民國89年於教務處下成立網路教務組…民國95年網路教務組與交大出版社正式合併成『數位內容製作中心』」；DCPC 服務項目含「網路教學平台的開發與維運、平台內全校課程的建置、全校老師與學生的帳號建立」。之後 e.nctu.edu.tw（2007-12）與 e2.nctu.edu.tw（2021 存檔）都轉址到 dcpc.nctu.edu.tw。

---

## 5. www.nctu.edu.tw 怎麼連到 e／e2／e3（2001–2009）

| 存檔 | 位置 | 連結文字 → 目標 |
|---|---|---|
| 2001-02（20010203151100） | 首頁為「NCTU Resource Directory 網站指引」 | 沒有 e.nctu 連結 |
| 2002-01、2003-02、2003-08 | 首頁 | 「**網路大學 e.nctu**」→ http://e.nctu.edu.tw/ |
| 2002-02、2005-02、2007-02 | 校園資訊 `campus/index.html` | 「**交大網路校園**」→ http://e.nctu.edu.tw（2006 之後實際會轉到 E3／DCPC） |
| 2009-02 | campus/index.html | 已無「交大網路校園」 |
| 2003-09（online-index.htm 最早存檔；首頁何時改連此頁不確定，2003-08 首頁仍是「網路大學 e.nctu」） | 「NCTU 線上學習」`HTM/online-index.htm`（frameset，內容框 online-content.htm） | 內容框列「e.nctu網路校園」、網路教務組、網路學習碩士在職專班、台灣網路大學系統… |
| 2004-07 | 首頁 | 「NCTU 線上學習」→ HTM/online-index.htm（首頁不再直接連 e.nctu） |
| 2005-02 | 首頁 →「NCTU 線上學習」`NCTU-Online/online-index.htm` | 列 **e2.nctu.edu.tw**、**bb.nctu.edu.tw** 等（圖片連結） |
| 2006-04 | `www.cc.nctu.edu.tw/~nacad/nctu_online/` | bb、e2、**e3.nctu.edu.tw** 三者並列 |
| 2007-02 / 2007-03 | 首頁 → `~nacad/nctu_online/` | alt：「e3網路教學平台」「e2網路教學平台」「BlackBoard網路教學平台」 |
| 2008-08、2009-02 | 首頁 | 「**BB教學平台**」→ bb.nctu.edu.tw、「**e3教學平台**」→ http://e3.nctu.edu.tw/NCTU_E3/lms2/、「NCTU線上學習」→ dcpc.nctu.edu.tw/nctu_online/ |

使用者描述的路徑「2005 首頁 → 生活資訊/校園資訊 → 交大網路校園 → 關於本站」，和 2005-02 首頁「校園資訊」浮動選單文字（「…網路大學系統聯盟、**交大網路校園**、電子郵件D2系統、互動式遠距教學」）及 campus/index.html 的連結一致。但 2005 年時 e.nctu.edu.tw 本身已經不再更新，最後內容存檔是 2004-02。

---

## 6. 圖片清單

存放於 `/Users/em/Desktop/nctu-e3-history/images/`。截圖用全域 Playwright CLI 1.63.0（`playwright screenshot --full-page`），用 Wayback `if_` 模式（不含工具列、資源經 Wayback 改寫），視窗 1024×768。

| 檔名 | 內容 | Wayback 來源 |
|---|---|---|
| **e（E.NCTU）** |  |  |
| e_2000-12_home.png | V1.0 時期首頁 index_new.htm；切圖多數未被存檔，只剩文字（最新消息 10/17–11/23） | https://web.archive.org/web/20001206215100/http://e.nctu.edu.tw/index_new.htm |
| e_2001-02_home.png | 新年版首頁（index_newyear）；圖檔未存檔 | https://web.archive.org/web/20010215005310/http://e.nctu.edu.tw/index_new.htm |
| e_2001-06_home.png | **代表圖**：2001-04 改版綠色首頁＋E.NCTU NEWS＋人氣排行榜（完整） | https://web.archive.org/web/20010619061708/http://e.nctu.edu.tw/index_new.php |
| e_2002-02_home.png | 2002 年版首頁（2002_new.gif 版型，中間 Flash 未存檔，顯示為 Ruffle 佔位圖） | https://web.archive.org/web/20020211224220/http://e.nctu.edu.tw/index_new.php |
| e_2003-12_home.png | 最後版本首頁（只剩兩則公告） | https://web.archive.org/web/20031203233453/http://e.nctu.edu.tw/index_new.php |
| e_2003-12_profile.png | **關於本站** Profile.htm 全頁（使用者找到的起點） | https://web.archive.org/web/20031204104846/http://e.nctu.edu.tw/news/Profile.htm |
| e_2004-02_teamgroup.png | 工作團隊 | https://web.archive.org/web/20040212014131/http://e.nctu.edu.tw/teamgroup/index.htm |
| e_2004-02_sitemap.png | E.NCTU 網站導覽（個人工作室／組織建館功能表） | https://web.archive.org/web/20040212011833/http://e.nctu.edu.tw/property/service/system/map.php |
| e_2001-06_orglist.png | 組織管理（組織列表：89 學年課程、行政／研究／教學單位、社團） | https://web.archive.org/web/20010625111841/http://e.nctu.edu.tw/org/orglist.php |
| e_2002-04_bbs_phorum.png | 課程討論區（Phorum，Java程式設計 1099） | https://web.archive.org/web/20020425075307/http://e.nctu.edu.tw/bbs/list.php?f=1271&t=1&a=1 |
| e_2001-03_profile_image001.png | E.NCTU logo（Profile 頁圖檔，下載） | https://web.archive.org/web/20010302091059im_/http://e.nctu.edu.tw/news/Profile.files/image001.png |
| e_2001-03_profile_functions.jpg | 系統定位圖：人流／知識流／資訊流（下載） | https://web.archive.org/web/20010302091059im_/http://e.nctu.edu.tw/news/Profile2.files/image008.jpg |
| e_2001-03_profile_architecture.jpg | E.NCTU 系統平台架構圖（IE 4.0、FreeBSD＋PHP、PostgreSQL）（下載） | https://web.archive.org/web/20010302091059im_/http://e.nctu.edu.tw/news/Profile.files/image010.jpg |
| e_2001-06_header_r01_c01.jpg | 2001 版首頁左上 banner「e.nctu.edu.tw」（下載） | https://web.archive.org/web/20010619061708im_/http://e.nctu.edu.tw/HTML/Index/200104/index_2001_r01_c01.jpg |
| **e2（eCampus）** |  |  |
| e2_2002-10_login.png | 最早登入頁（含「火線討論區」、選身份）。Wayback 直接顯示會出現 internal error，所以改成**本機重建**：取 `id_` 原始 HTML、移除 script、圖片改指向 `im_` 存檔後截圖；左上 ecampus logo 該時間點沒載到 | https://web.archive.org/web/20021010082927id_/http://e2.nctu.edu.tw/eCampus/default.aspx |
| e2_2003-01_login.png | **代表圖**：登入頁（ecampus logo＋交大校徽、選身份、2002/12/25 上傳元件公告） | https://web.archive.org/web/20030109212507/http://e2.nctu.edu.tw/eCampus/ |
| e2_2006-04_login.png | 4.0.2005.0217 版登入頁（template_02），同樣是**本機重建**（Wayback 頁面載入會卡住）；校徽圖沒載到 | https://web.archive.org/web/20060423035328id_/http://e2.nctu.edu.tw/ecampus/default.aspx |
| e2_2004-09_course-signup.png | 台灣聯合大學網路教學課程 選課登錄系統（e2 主機上的 course.asp） | https://web.archive.org/web/20040907042736/http://e2.nctu.edu.tw/Course/course.asp |
| e2_2005-06_help_popup.png | 操作說明：設定快顯封鎖程式（說明圖未存檔） | https://web.archive.org/web/20050617033051/http://e2.nctu.edu.tw/ECAMPUS_HELP/%E8%A8%AD%E5%AE%9A%E5%BF%AB%E9%A1%AF%E5%B0%81%E9%8E%96%E7%A8%8B%E5%BC%8F.htm |
| e2_2007-08_dcpc_e2-end-notice.png | **DCPC 公告「E2網路教學平台提供服務至九月底止，請教師們轉用E3平台」內文** | https://web.archive.org/web/20070917181422/http://dcpc.nctu.edu.tw/popup.aspx?type=1&id=3e3137da-d804-4c49-a4aa-4ebde347c987 |
| e2_2002-10_logo.gif | e2「ecampus」logo（131×35，下載） | https://web.archive.org/web/20021010143020im_/http://e2.nctu.edu.tw:80/eCampus/img/sys/logo.gif |
| e2_2002-10_campus-logo.gif | e2 交大校徽＋「國立交通大學」字樣（229×35，下載） | https://web.archive.org/web/20021010142549im_/http://e2.nctu.edu.tw:80/eCampus/img/sys/campus-logo.gif |
| e2_2006-04_bg_logo.gif | template_02 版 ecampus logo（下載） | https://web.archive.org/web/20060429233525im_/http://e2.nctu.edu.tw:80/eCampus/img/template_02/bg/bg_logo.gif |
| e2_2006-04_bg_logo_school.gif | template_02 版校徽（下載） | https://web.archive.org/web/20060429233515im_/http://e2.nctu.edu.tw:80/eCampus/img/template_02/bg/bg_logo_school.gif |
| **www.nctu.edu.tw** |  |  |
| www_2002-01_home.png | 交大首頁，「資訊捷徑」裡有「網路大學e.nctu」（頁尾的訪客計數器和「最近更新日期」是 JS 動態產生，顯示的是截圖當天日期，不是存檔日期） | https://web.archive.org/web/20020126120653/http://www.nctu.edu.tw/ |
| www_2005-02_campus-info.png | 「校園資訊」頁：電腦網路 →「交大網路校園」（e.nctu.edu.tw） | https://web.archive.org/web/20050208093948/http://www.nctu.edu.tw/campus/index.html |
| www_2009-02_home.png | 交大首頁 2009-02（「BB教學平台」「e3教學平台」在下拉選單裡，截圖上看不到） | https://web.archive.org/web/20090203092419/http://www.nctu.edu.tw/ |

截圖未成功、已刪除的：e2 2003-08 登入頁（Wayback 回「This snapshot cannot be displayed due to an internal error」）、`~nacad/nctu_online/` 2007-03（整頁是 image map，存檔圖檔缺失，截出空白）。

同一個資料夾裡其他 `wayback_*`、`e3_*`、`live_*` 等檔案是其他研究分支產生的，不在本筆記範圍；其中 `wayback_2007-09-11_dcpc_home_E2_end_notice.png` 是 DCPC 首頁含上述公告列表的截圖，可和 `e2_2007-08_dcpc_e2-end-notice.png` 對照。

---

## 7. 未解問題／後續可查

- e2 eCampus 的**開發廠商**：存檔頁面沒有寫。可查網路教務組 2002 年會議紀錄、採購公告，或 e2 的 `css`／`.aspx` 原始碼註解（目前存檔的 css 只有 font.css／Main.css）。
- e2 伺服器實際關機日期（公告停止服務為 2007-09 底，但存檔顯示 2009-07 頁面仍在）。
- E.NCTU 的總帳號數／課程數：沒有找到統計頁。
- `ws01.doc`（網路教學工作坊一）、`n2.doc`（網路教學教師手冊 E.NCTU，90.09）等 Word 檔可試著從 Wayback 下載（`www.cc.nctu.edu.tw/~nacad/news/`）。
- 2004-02 ~ 2006-05 之間 e.nctu.edu.tw 的狀態（沒有根目錄存檔）。
