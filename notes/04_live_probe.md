# 04 實測：哪些舊 E3／數位學習系統 2026-10 仍在線上

- 實測時間：2026-10-16 00:18–00:45（台北時間，UTC+8；伺服器 `Date` 標頭為 2026-10-15 16:32 GMT）
- 實測位置：校外網路，解析器 1.1.1.1，並以 8.8.8.8 交叉驗證
- 方法：只做被動查詢與一般 HTTP GET/HEAD（`dig +short`、`curl -sI/-s -m 15 -L`、TLS 握手讀憑證、crt.sh、Cert Spotter、HackerTarget）。沒有登入、沒有猜帳密、沒有掃 port、沒有繞過存取控制。
- 共測 157 個主機名（猜測變體 141 個，加上 CT 與被動來源找到的 16 個）。

## 一句話結論

**交大時代（`*.nctu.edu.tw`）與陽明時代（`*.ym.edu.tw`）的數位學習主機已全部從 DNS 移除（NXDOMAIN），沒有一個還連得到。** 還在線上的「舊系統」只有一個：**`e3.nycu.edu.tw`，即 2021–2024 年的陽明交大 E3**。它是 `e3new.nctu.edu.tw`（新 E3）直接延續下來的 Moodle 站，伺服器還在跑，但登入頁已加上 `<meta refresh>`，一般瀏覽器開啟會被立刻導到現行的 `e3p.nycu.edu.tw`，所以使用者「找不到」它。另外，開放式課程 `ocw.nycu.edu.tw` 仍提供交大時期（如 103 學年度）的課程內容，但網站本身已是 NYCU 新版 WordPress，不是舊系統。

## 1. 仍有 DNS 紀錄的主機（17 個）

| 主機 | DNS | HTTP（http / https） | 轉址目標 | Server | title | 判讀 |
|---|---|---|---|---|---|---|
| **e3.nycu.edu.tw** | 140.113.41.24 | http：逾時（port 80 無回應）／https：303 → 200 | `/` → `/login/index.php`（Moodle 303）；頁內 `<meta http-equiv="refresh" content="0; url=https://e3p.nycu.edu.tw/">` | nginx | E3 數位教學平台: 登入本網站 | **舊 E3（2021–2024），伺服器仍在線**。Moodle，佈景 `theme/dcpc`（`dcpc2021.css?20211025`，dcpc 為交大新 E3 的自製佈景），YUI 3.17.2（Moodle ≤ 4.2 的特徵），`themerev=1721015251` → 2024-07-15 11:47（最後一次清快取／改版）。頁尾「Copyright ©2022 國立陽明交通大學 教學資源組」。校外帳號用 Google Authenticator 二階段驗證；Portal 入口為 `portal.nycu.edu.tw/portal/newe3`。瀏覽器開啟會 0 秒轉到 e3p，因此實務上**不可用、只剩伺服器存活**。 |
| **e3p.nycu.edu.tw** | 140.113.41.110 | http：逾時／https：303 → 200 | `/` → `/login/index.php` | （無 Server 標頭） | 登入本網站 \| E3@NYCU | **現行 E3（2024–）**。Moodle，佈景 `boost_union`，YUI 3.18.1（Moodle ≥ 4.3 的特徵），`themerev=1792018959` → 2026-10-15。校外帳號改用 Email 6 位數驗證碼；Portal 入口 `portal/newe3p`；有「以訪客身分登入」。 |
| eportfolio.nycu.edu.tw | 140.113.41.73 | http：逾時／https：200 | 前端 JS 導到 `portal.nycu.edu.tw/#/login` | （無；F5 BIG-IP 型 `TS…` cookie） | NYCU e-Portfolio | 學習歷程系統的 **NYCU 新版**（Vite 打包的 SPA，`/assets/index.*.js`），不是 2014 年的 `eportfolio.nctu.edu.tw`。需登入。 |
| ocw.nycu.edu.tw | 140.113.199.202 | 200（http→https 301） | `https://ocw.nycu.edu.tw/` | Apache | 首頁 - NYCU OCW | 開放式課程，**現行**。WordPress（Soledad/Penci 佈景），頁尾 ©2026，諮詢單位「教務處 數位教學中心」。首頁「熱門課程」仍是交大時期的「微積分(一) 103學年度 莊重老師」「電子學(一)(二) 陳振芳老師」等，**內容是舊 OCW 的延續，平台不是**。不需登入。 |
| video.ocw.nycu.edu.tw | 140.113.8.88 | 200 / 200 | — | Microsoft-IIS/10.0 | IIS Windows Server | OCW 影音主機，首頁只是 IIS 預設頁（影片檔另以路徑提供）。憑證 2026-09-29 剛續簽，仍在用。 |
| portal.nycu.edu.tw | 140.113.41.157 | http：逾時／https：200 | — | — | 國立陽明交通大學 校園單一入口 NYCU Portal | 單一入口，非 E3 本體；`/portal/newe3`、`/portal/newe3p` 兩個入口代號可證明兩代 E3 並存過。 |
| ctld.aa.nycu.edu.tw | 140.113.8.70 | 逾時 / 逾時 | — | — | — | 教學發展中心相關主機，校外連不到。 |
| ctldgt.aa.nycu.edu.tw | 140.113.8.18 | 403 / 403 | — | Microsoft-IIS/8.5 | 403 - 禁止 | 教學發展中心內部系統（IIS 8.5 ≈ Windows Server 2012 R2），拒絕存取，與 E3 無直接關係。 |
| ctldbase.aa.nycu.edu.tw | 140.113.199.22 | http 200 / https 連線中斷 | meta refresh → `/cgi-sys/defaultwebpage.cgi` | Apache | （無） | cPanel 預設頁，空站。 |
| minicourse.ict.nycu.edu.tw | 140.113.199.123 | http 中斷 / https 200 | — | nginx/1.29.4 | ICT課程管理系統 | 資訊學院短期課程管理，非 E3 系列。 |
| lms.cesh.nycu.edu.tw | 140.113.199.155 | 200 | → https | Microsoft-IIS/10.0 | 交大實驗室環安管理系統 | 名稱有 lms，但是「實驗室環安管理系統」，與教學平台無關。 |
| lms2.lab.nycu.edu.tw | 140.113.30.131 | 200 | → https | Apache/2.4.37 (CentOS Stream) | LMS2 Server Status | 實驗室伺服器狀態頁，與教學平台無關。 |
| vod.ece.nycu.edu.tw | 140.113.237.8 | 逾時 / 逾時 | — | — | — | 電機學院 VOD，校外連不到。 |
| ep.nycu.edu.tw | 140.113.199.170 | 200 | → https | nginx | 國立陽明交通大學電子物理系 | 電子物理系，與 e-portfolio 無關（對照組）。 |
| mochi.life.nctu.edu.tw | 140.113.120.221 | 200 | → https | nginx/1.25.0 | MOCHI | 生科實驗室工具。列出來是因為它是極少數**還能解析的 nctu.edu.tw 主機**（見第 3 節）。 |
| nctu-alumni-voice.sec.nycu.edu.tw | 140.113.199.20 | 200 | → https | Apache | 交大友聲雜誌社 | 對照組，非教學平台。 |
| www.nycu.edu.tw | Cloudflare | 200 | `/nycu/ch/index` | cloudflare | 國立陽明交通大學 | 對照組（確認網路正常）。 |

## 2. 查無 DNS 的主機（140 個，全部 NXDOMAIN）

以 1.1.1.1 與 8.8.8.8 交叉確認，回應都是 `status: NXDOMAIN`（不是逾時或 SERVFAIL），表示紀錄已被刪除，不是暫時故障。`nctu.edu.tw` 與 `ym.edu.tw` 的權威 DNS 都已是 `ns1/ns2.nycu.edu.tw`，SOA 序號分別為 `2026090202` 與 `2026062401`，代表 zone 仍有人維護，但這些名稱已移除。`ymu.edu.tw` 整個網域都不存在。

| 類別 | 主機 | DNS | HTTP | 判讀 |
|---|---|---|---|---|
| 歷代正式主機 | e.nctu.edu.tw、e2.nctu.edu.tw、e3.nctu.edu.tw、e3new.nctu.edu.tw、eportfolio.nctu.edu.tw、ocw.nctu.edu.tw | NXDOMAIN | 無法連線 | 2001 交大網路校園、2002–2009 e2、舊 E3（2006–2019）、新 E3（2017–2020）、交大 e-Portfolio、交大 OCW：**全部下線**，網域層級也不再轉址。 |
| CT 找到的交大舊名 | moodle.nctu.edu.tw、moodle6.nctu.edu.tw、learntech.nctu.edu.tw、www.learntech.nctu.edu.tw | NXDOMAIN | — | 2014 年短暫存在的 Moodle 測試機、學習科技站，已下線。 |
| nctu.edu.tw 猜測變體 | e1、e4、e3old、olde3、e3-old、e3history、e3archive、e3p、e3plus、e3m、e3mobile、m.e3、e3app、e3t、e3test、e3-test、e3dev、e3beta、e3lab、e3video、e3cs、cs-e3、e3sync、e3api、e3static、e3file、e3vod、e3p-dev、e3ptest、newe3、e3v、e3x、e3web、e3s、e3n、e3a、e3b、ee3、ecourse、ecourse2、elearning、ecampus、elearn、moodle、ilearn、lms、ilms、dcpc（皆 `.nctu.edu.tw`） | NXDOMAIN | — | 不存在。 |
| nycu.edu.tw 猜測變體 | e、e1、e2、e4、e3old、olde3、e3-old、e3history、e3archive、e3new、e3plus、e3m、e3mobile、m.e3、e3app、e3t、e3test、e3-test、e3dev、e3beta、e3lab、e3video、e3cs、cs-e3、e3sync、e3api、e3static、e3file、e3vod、e3p-dev、e3ptest、newe3、e3v、e3x、e3web、e3s、e3n、e3a、e3b、ee3、ecourse、ecourse2、elearning、ecampus、elearn、moodle、ilearn、lms、ilms、dcpc（皆 `.nycu.edu.tw`） | NXDOMAIN | — | 不存在。沒有「e3 歷史備份站」之類的公開主機。 |
| 陽明舊平台 | e、e3、elearning、moodle、lms、ecourse、ecampus、elearn、ilearn、ocw、www × {`ym.edu.tw`、`web.ym.edu.tw`、`ymu.edu.tw`}（33 個） | NXDOMAIN | — | 陽明舊數位學習平台已全部下線；連 `www.ym.edu.tw` 都已 NXDOMAIN。另查到 2020 年陽明校內公告：配合合校，自 108-2 學期引進交大 New E3，原陽明 eCampus 自 109-1 起停止服務。 |

## 3. 憑證透明度（CT）與被動子網域資料

### 查詢方式與限制

- crt.sh 已不支援 `%e3%` 這類**中間萬用字元**（回傳 `Unsupported use of '%'`），所以改抓 `%.nctu.edu.tw`、`%.nycu.edu.tw`、`%.ym.edu.tw` 全量，再在本機過濾，並對每個關鍵主機名做精確查詢。
- crt.sh 全量結果有截斷：nctu 3,045 筆（2006-03 至 2018-09）、nycu 2,554 筆（只到 2022-02）。因此 nycu 的近期名稱改用 Cert Spotter（SSLMate）補齊，只含**目前有效**的憑證，共 842 張、581 個名稱。Cert Spotter 查 nctu 時被限流。
- **e3.nycu.edu.tw、e3p.nycu.edu.tw、e3new.nctu.edu.tw 在 CT 裡沒有專屬憑證**：它們用的是 `*.nycu.edu.tw`／`*.nctu.edu.tw` 萬用字元憑證，所以**無法從 CT 推定上線日期**。
- HackerTarget hostsearch 免費版每個網域只回 50 筆，其中沒有 e3 相關主機。

### CT 中與數位學習相關的主機名

| 主機名 | 最早憑證（not_before） | 最晚憑證到期 | 簽發者 | 現況 | 備註 |
|---|---|---|---|---|---|
| e3.nctu.edu.tw | **2014-08-28** | 2021-09-13 | TWCA（2014）→ ZeroSSL（2021-03-22、2021-06-15） | NXDOMAIN | 2014 是 crt.sh 收錄的第一張專屬憑證；2021 年合校後還換成 ZeroSSL 免費憑證續用（推測只剩轉址用途），2021-09 之後沒有再續簽。 |
| moodle6.nctu.edu.tw | 2014-08-01 | 2015-08-06 | TWCA | NXDOMAIN | 2014 年的 Moodle 測試／建置機。 |
| moodle.nctu.edu.tw | 2014-09-02 | 2014-10-02 | TWCA | NXDOMAIN | 只有一個月的試用憑證。 |
| eportfolio.nctu.edu.tw | 2014-09-17 | 2015-09-17 | TWCA | NXDOMAIN | 交大 e-Portfolio 的 HTTPS 化時間點。 |
| learntech.nctu.edu.tw（含 www/mail/webmail/webdisk/cpanel） | 2018-05-03 | 2018-11-18 | cPanel, Inc. Certification Authority | NXDOMAIN | 學習科技相關 cPanel 站。 |
| ocw.nctu.edu.tw | 2020-07-20 | 2023-01-03 | TWCA → ZeroSSL（2022-10-05） | NXDOMAIN | 交大 OCW，合校後到 2022 年底仍續用。 |
| video.ocw.nycu.edu.tw | **2021-03-25** | 2027-04-12 | TWCA，每年續簽 | 在線 | NYCU OCW 影音主機，2021-03 已上線。 |
| ocw.nycu.edu.tw | 2024-01-18（專屬憑證） | 2026-11-12 | TWCA | 在線 | 2024 年以前應是用 `*.nycu.edu.tw` 萬用字元憑證。 |
| *.nycu.edu.tw（萬用字元） | 2020-12-09（crt.sh 截斷範圍內最早） | — | TWCA | 使用中 | e3、e3p、eportfolio 目前都掛這張。 |
| lms.cesh.nycu.edu.tw、lms2.lab.nycu.edu.tw、vod.ece.nycu.edu.tw、minicourse.ict.nycu.edu.tw、ctldgt.aa.nycu.edu.tw | （Cert Spotter，目前有效） | — | — | 見第 1 節 | 名稱相近，但都不是 E3 系列。 |

### 實測時讀到的 TLS 憑證（2026-10-16）

| 主機 | 憑證 CN | 簽發者 | 生效 | 到期 |
|---|---|---|---|---|
| e3.nycu.edu.tw | *.nycu.edu.tw | TWCA Secure SSL Certification Authority | 2025-10-20 | **2026-10-20** |
| e3p.nycu.edu.tw | *.nycu.edu.tw | TWCA SSL Certification Authority（SSL Sub-CA） | 2026-10-05 | 2027-04-21 |
| eportfolio.nycu.edu.tw | *.nycu.edu.tw | TWCA SSL Certification Authority | 2026-10-01 | 2027-04-17 |
| ocw.nycu.edu.tw | ocw.nycu.edu.tw | TWCA Secure SSL Certification Authority | 2025-11-12 | 2026-11-12 |
| video.ocw.nycu.edu.tw | video.ocw.nycu.edu.tw | TWCA SSL Certification Authority | 2026-09-29 | 2027-04-12 |

**注意**：e3p 與 eportfolio 都在 2026-10 初換上新的萬用字元憑證，**唯獨 e3.nycu.edu.tw 仍掛 2026-10-20 到期的舊憑證**。如果沒有更新，舊 E3 主機約 4 天後就會出現憑證錯誤，可能也代表它即將退役。要存證就要趁現在。

### 還能解析的 nctu.edu.tw 主機

把 CT 裡 1,109 個不重複的 `*.nctu.edu.tw` 名稱全部 `dig` 一次，只剩 13 個能解析，而且全是系所郵件或實驗室主機：csmail/mail/imap/pop3/smtp/linux/farewell.cs、iclab.life、d2、edoc2、mscnc、pop3。**沒有任何數位學習主機。**

## 4. 舊 E3（e3.nycu.edu.tw）的細節證據

- `GET https://e3.nycu.edu.tw/` → `HTTP/2 303`、`x-redirect-by: Moodle`、`Location: /login/index.php`，並設定 `MoodleSession` cookie。這代表 **Moodle 應用程式本身在運作**，不是靜態轉址頁。
- 登入頁 HTML 內含 `<meta http-equiv="refresh" content="0; url=https://e3p.nycu.edu.tw/" />`，所以瀏覽器 0 秒內會跳到 e3p。用 Playwright 追蹤，導覽鏈為：303 e3 → 200 e3/login → 303 e3p → 200 e3p/login。
- `M.cfg`：`wwwroot=https://e3.nycu.edu.tw`、`theme=dcpc`、`jsrev/templaterev=1721015251`（2024-07-15）。
- `https://e3.nycu.edu.tw/webservice/rest/server.php`（不帶 token）回 Moodle XML `invalidtoken`，表示 Web Service 層也還活著（只做了一次無參數 GET 確認是否存活，沒有嘗試任何 token）。
- `/login/forgot_password.php` 回 `503`（「無效的使用者」），表示忘記密碼功能已關閉。
- `/course/index.php`、`/course/search.php` → 303 導回登入頁，訪客無法瀏覽課程目錄。
- `/theme/dcpc/style/dcpc2021.css?20211025` 仍可下載（200，21,888 bytes），可作為 2021 年佈景的存檔。
- `lib/upgrade.txt` 404、`admin/environment.xml` 403，所以無法取得精確的 Moodle 版本號；只能從 YUI 版本判斷「≤ 4.2」。

## 5. 截圖清單

都存在 `/Users/em/Desktop/nctu-e3-history/images/`，用全域 Playwright（`/Users/em/.nvm/versions/node/v26.8.2/bin/playwright`）拍攝，未安裝到任何專案。

| 檔案 | 內容 | 拍攝方式 |
|---|---|---|
| `live_e3.nycu.edu.tw_2026-10.png` | **舊 E3 登入頁原貌**：「國立陽明交通大學 數位教學平台」、帳號／密碼／驗證碼三欄、Google Authenticator 說明、頁尾「Copyright ©2022 國立陽明交通大學 教學資源組 版權所有」 | 用 Playwright 腳本（scratchpad 中的 `shot_norefresh.js`，`require` 全域 playwright 模組）攔截前往 e3p 的導覽並回 204，讓瀏覽器停在伺服器實際回傳的頁面。**頁面內容沒有修改**，只是阻止 meta refresh 跳走。 |
| `live_e3.nycu.edu.tw_redirected-to-e3p_2026-10.png` | 一般瀏覽器開 https://e3.nycu.edu.tw/ 的結果：已被導到 e3p 的登入頁 | `playwright screenshot --full-page --wait-for-timeout 4000`；用來證明一般使用者看不到舊頁面。 |
| `live_e3p.nycu.edu.tw_2026-10.png` | 現行 E3@NYCU 登入頁（boost_union 佈景，Email 驗證碼說明） | `playwright screenshot --full-page --wait-for-timeout 4000` |
| `live_eportfolio.nycu.edu.tw_2026-10.png` | e-Portfolio 被導到 NYCU 單一入口登入頁 | 同上 |
| `live_ocw.nycu.edu.tw_2026-10.png` | NYCU OCW 首頁全頁，含 103 學年度交大課程 | 同上 |
| `live_video.ocw.nycu.edu.tw_2026-10.png` | OCW 影音主機的 IIS 預設頁 | 同上 |

截圖都已逐張開啟確認內容正常。兩張 e3／e3p 的 meta refresh 版本像素完全相同，這也印證了轉址。

## 6. 原始資料（暫存）

原始輸出放在 `/private/tmp/claude-501/-Users-em-Desktop/ef64c714-0ca3-493b-bc59-04ddbcca6a4f/scratchpad/`：`dns.txt`、`nx_status.txt`、`http_summary.txt`、`http/*.hdr|*.body`、`ct/*.json`、`ct/flat.tsv`、`cs/*.json`、`nctu_alive.txt`。這是暫存目錄，若要長期保存，需要另外複製到本專案。
