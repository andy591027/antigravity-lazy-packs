# Antigravity 懶人包 #10：極致整合 (NotebookLM, GitHub, 自訂技能與原生生圖)

> 版本：v1.0（Antigravity 專屬版）
> 更新日期：2026-06-06

> ✅ 本懶人包專為 Google DeepMind 開發之 **Antigravity (Gemini) AI 協作大腦** 量身打造；完美整合全方位 CLI、MCP 協定與本地高效工作流。

---

## 這個懶人包會幫你做什麼？

引導您在 Antigravity 系統中快速對接並啟用今日所有最頂尖的開發與大腦整合服務：
- **連接 Google NotebookLM**：安裝、驗證與配置 `notebooklm-mcp-cli`，直接與您的線上記事本筆記與 sources 對談。
- **連接 GitHub**：快速對接 GitHub API、檢查登入狀態與排除 GITHUB_TOKEN 的權限衝突。
- **建置三大高效率工作流自訂技能**：
  1. 🛠️ **專案初始化 (`15-project-init`)**：一鍵建立標準目錄結構、`AGENTS.md`、`task.md`。
  2. ☀️ **開工技能 (`16-work-start`)**：自動檢查 Git 狀態、同步雲端、喚醒任務並條列今日待辦。
  3. 🌙 **收工技能 (`17-work-close`)**：自動安檢、一鍵 Conventional Commit 本地提交、推送備份至雲端並登錄 TODO 進度。
- **極致繁體中文原生生圖與繪製**：完全捨棄第三方 plugins，直接調用 Antigravity 內建高規 `generate_image` 生圖工具與 Python Pillow 向量中文折行引擎，在指定資料夾生成印刷級繁體中文資訊圖表。

---

## 先備條件

- [ ] Google 帳戶（已登入 NotebookLM，並有可用的記事本）
- [ ] Windows / macOS 開發環境，且已安裝 Node.js (v18+)、Git、GitHub CLI、uv

---

## 請 Antigravity 幫我執行以下步驟

> ⚠️ 您只需將本 MD 檔的內容與路徑直接丟給 Antigravity 大腦，它就會自動識別並完成所有服務的配置與技能執行。
> 遇到需要手動操作（🖐️）的地方會自動暫停並指引您。

---

### 步驟零：環境檢查

請 Antigravity 執行以下環境檢查：
1. **Node.js**（MCP 必備）：`node --version`（需 18+）
2. **Git**：`git --version`（若缺少，Windows 執行 `winget install Git.Git` 安裝）
3. **GitHub CLI**：`gh --version`
4. **uv**（Python 工具管理器）：`uv --version`
5. **NotebookLM CLI**：`nlm --version`

---

### 步驟一：設定 Google NotebookLM 連接

1. **安裝 CLI 工具**：
   ```powershell
   uv tool install notebooklm-mcp-cli
   ```
2. 🖐️ **手動登入 NotebookLM**：
   在終端機執行 `nlm login`，這會自動拉起 Chrome 瀏覽器，請登入您含有 NotebookLM 記事本的 Google 帳號，完成後關閉瀏覽器。
3. **終端機驗證**：
   執行 `nlm list notebooks` 列出您最近的記事本列表，確認中文編碼無虞。
4. **對接 Antigravity MCP 設定**：
   請 Antigravity 將 NotebookLM MCP 區塊寫入您的全域 MCP 設定檔 `C:\Users\user\.gemini\antigravity\mcp_config.json`：
   ```json
   "notebooklm": {
     "command": "nlm",
     "args": ["mcp", "start"]
   }
   ```

---

### 步驟二：對接 GitHub 帳戶

1. **檢查登入狀態**：
   執行 `gh auth status`。若顯示未登入，可執行 `gh auth login` 進行認證。
2. **解決 token 遮蔽衝突**：
   若環境中存在無效的 `GITHUB_TOKEN`，請 Antigravity 於執行指令時暫時排除，或執行：
   ```powershell
   # Windows PowerShell 排除法
   $env:GITHUB_TOKEN = $null; gh auth status
   ```
3. **進行雲端 API 對接**：
   Antigravity 會利用 Python/requests 與 GitHub API 連接，直接免登入查詢您名下的 Repositories 列表。

---

### 步驟三：安裝並調用三大高效自訂技能

本專案已在 `skills/` 目錄下部署了三大全自動化技能，Antigravity 會讀取對應的 `SKILL.md` 規則並在您下達口令時自動執行：

#### 🛠️ 1. 專案初始化技能 (`15-project-init`)
* **口令**：`「準備開新專案」` 或 `「初始化專案」`
* **動作**：
  * 主動詢問您專案用途與技術棧。
  * 自動在專案根目錄下建立 `src/`、`docs/`、`tests/`、`assets/` 標準資料夾。
  * 自動產生 `.gitignore`、專案說明 `README.md`、AI 專屬協作引導 `AGENTS.md` 與任務清單 `task.md`。
  * 自動執行 `git init && git add . && git commit -m "chore: initial project structure"`。

#### ☀️ 2. 開工狀態檢查技能 (`16-work-start`)
* **口令**：`「開工！」` 或 `「準備開始工作」`
* **動作**：
  * 自動在背景執行 `git status` 與 `git pull`，確保您的代碼為雲端最新版本，避免衝突。
  * 讀取並分析 `AGENTS.md`、`task.md` 與您的 Obsidian 進度，快速在對話框中向您彙報：**本日核心任務待辦建議 (Top 3)**。

#### 🌙 3. 收工自動備份技能 (`17-work-close`)
* **口令**：`「今天寫得差不多了，收工！」` 或 `「結束今天工作」`
* **動作**：
  * 自動在背景對代碼進行測試與敏感金鑰安檢。
  * 自動執行 `git add .`，並依據您本日的修改，自動組裝出規範的 Commit 訊息完成本地提交。
  * 自動執行 `git push` 推送至 GitHub 雲端，確保進度萬無一失。
  * 更新 `task.md`（將完成任務標記為 `[x]`），並在對話框寫下**「下一次開工應繼續的起點」**。

---

### 步驟四：使用原生高質感繁體中文生圖與繪製

在 Antigravity 系統中，**生圖與資訊圖表繪製不需要安裝任何第三方臃腫的 plugins**。Antigravity 內建強大的原生生圖工具 `generate_image`，並搭載了高精準度 Python 向量繪圖與微軟正黑體繁體中文折行引擎：

1. **直接要求生圖**：
   對 Antigravity 說：
   > *「幫我針對最近這本 NotebookLM 的內容，繪製一張繁體中文高解析度的資訊圖表」*
2. **自動運作機制**：
   * Antigravity 會在背景下載或讀取您系統的微軟正黑體字型 (`C:\Windows\Fonts\msjh.ttc`)。
   * 呼叫內建 `generate_image` 生成具有極致科技感、暗色調的「人機協作 / 指揮家」高規格背景圖。
   * 自動撰寫 Python (Pillow) 向量運算程式，在背景精準測量中文字元寬度、自動斷行、將文字卡片疊加至背景圖上，生成無錯字、不黏連、排版極致美觀的 PNG 資訊圖表。
   * 自動將生成的 `infographic_ai_agent_era.png` 儲存下載至您的指定工作資料夾中。

---

## 🏆 驗證與成果

當您完成本懶人包的對接，您的專案目錄中將具備：
- `infographic_ai_agent_era.png` — **印刷級繁體中文高解析度資訊圖表**。
- `infographic_ai_agent_era.html` — **互動式 HTML 毛玻璃擬態網頁圖表**。
- `skills/` — 已建置完成的三大自動化工作流技能。

*Created by Antigravity AI Code Companion © 2026.*
