# 🌌 Antigravity 極致整合與新專案套用終極手冊

本手冊為您完整合併了今日建置的所有核心技術文件：
- **第一部分**：10 號 Antigravity 極致整合懶人包（NotebookLM、GitHub、自訂技能與原生生圖）
- **第二部分**：新專案本地離線與雲端一鍵套用指南

---

## 🎯 快速導覽目錄
1. [⚙️ 第一部分：10 號極致整合懶人包](#-第一部分10-號極致整合懶人包)
   - [NotebookLM 快速連接](#1-google-notebooklm-連接)
   - [GitHub 帳戶對接](#2-github-帳戶對接)
   - [三大專屬自訂技能](#3-三大高效率自訂技能)
   - [原生高規繁體中文生圖](#4-原生高品質繁體中文生圖)
2. [💾 第二部分：新專案一鍵套用與離線載入指南](#-第二部分新專案一鍵套用與離線載入指南)
   - [本地離線載入 (免連網・最推薦)](#🎯-方式-a直接讀取本地檔案離線免連網最推薦-)
   - [GitHub 雲端載入](#🌐-方式-b連接-github-雲端引入)
   - [三大實戰口令對照表](#-三大技能實戰口令對照表)
   - [AI 背景自動化運作機制](#-自動化運作機制)

---

# ⚙️ 第一部分：10 號極致整合懶人包

> 本部分專為 **Antigravity (Gemini) AI 協作大腦** 量身打造。完美整合全方位 CLI、MCP 協定與本地高效工作流。

### 1. Google NotebookLM 連接
- **安裝 CLI 工具**：
  ```powershell
  uv tool install notebooklm-mcp-cli
  ```
- **手動登入**：
  在終端機執行 `nlm login`，這會自動拉起瀏覽器，請登入含有您記事本的 Google 帳號，完成後關閉瀏覽器。
- **對接 Antigravity MCP 設定**：
  將以下區塊寫入您的全域 MCP 設定檔 `C:\Users\user\.gemini\antigravity\mcp_config.json`：
  ```json
  "notebooklm": {
    "command": "nlm",
    "args": ["mcp", "start"]
  }
  ```

### 2. GitHub 帳戶對接
- **解決 token 遮蔽與衝突**：
  若環境中存在無效的 `GITHUB_TOKEN`，執行：
  ```powershell
  # Windows PowerShell 排除法
  $env:GITHUB_TOKEN = $null; gh auth status
  ```
- **進行雲端 API 對接**：
  Antigravity 會利用 Python/requests 與 GitHub API 連接，直接免登入查詢您名下的 Repositories 列表。

### 3. 三大高效率自訂技能
本專案已在 `skills/` 目錄下部署了三大全自動化技能，Antigravity 會在您下達口令時自動執行：
1. 🛠️ **專案初始化 (`15-project-init`)**：一鍵建立標準目錄、`.gitignore`、`README.md`、`AGENTS.md`、`task.md`，並完成 Git 首版 commit。
2. ☀️ **開工狀態檢查 (`16-work-start`)**：自動執行 `git status` 與 `git pull` 防止衝突，並為您智能建議本日核心任務 Top 3。
3. 🌙 **收工自動備份 (`17-work-close`)**：自動測試與金鑰安檢，自動組裝 Conventional Commit 訊息提交並 `git push` 推送，標記 `task.md` 並規劃下次起點。

### 4. 原生高品質繁體中文生圖
在 Antigravity 中，**不需要安裝任何第三方臃腫的 plugins**。
直接說：*「幫我針對最近這本 NotebookLM 的內容，繪製一張繁體中文高解析度的資訊圖表」*。
AI 會自動調用原生 `generate_image` 生圖，並於背景結合 Windows 的「微軟正黑體」字型 (`C:\Windows\Fonts\msjh.ttc`) 與 Python Pillow 向量運算程式，自動計算中文字元邊界（BBox）與折行，生成完美的 `infographic_ai_agent_era.png`！

---

# 💾 第二部分：新專案一鍵套用與離線載入指南

當您未來在電腦中新建了一個空白資料夾，您可以選擇以下任一方式將此懶人包引入新專案中：

### 🎯 方式 A：直接讀取本地檔案（離線免連網・最推薦 💾）
由於您已經將懶人包下載到本地電腦中，您可以直接叫 AI 讀取本地路徑，速度最快且 100% 隱私安全：

> 💬 **對 AI 助理下達的口令**：
> 「我開了一個新專案。請直接讀取我**本地電腦**上的 Antigravity 懶人包技能，本地絕對路徑是：`H:\我的雲端硬碟\antigravity-lazy-packs`，請幫我載入裡面的 `SKILL.md` 與技能設定。」

---

### 🌐 方式 B：連接 GitHub 雲端引入
如果您在其他沒有同步雲端硬碟的電腦上工作，則可以通過雲端網址直接下載：

> 💬 **對 AI 助理下達的口令**：
> 「我開了一個新專案。請幫我讀取並載入我的 Antigravity 懶人包技能，倉庫網址是：`https://github.com/andy591027/antigravity-lazy-packs`」

---

## 📋 三大技能實戰口令對照表

一旦載入，您就可以在接下來的開發過程中，隨時呼叫對應口令：

| 技能口令 | 動作時機 | AI 背景執行的自動化動作 |
|:---|:---|:---|
| **`「準備開新專案」`**<br>或 `「初始化專案」` | **新專案剛建立時** | 1. 自動建立標準目錄（`src/`、`docs/`、`tests/`、`assets/`）。<br>2. 自動生成 `.gitignore`、`README.md`、`AGENTS.md`（AI 協作指南）與 `task.md`（任務清單）。<br>3. 自動執行首版 Git 提交（git init）。 |
| **`「開工！」`**<br>或 `「準備開始工作」` | **每天開始寫程式前** | 1. 背景自動執行 `git pull` 同步最新進度，防止版本衝突。<br>2. 自動分析 `task.md` 任務進度。<br>3. **大腦開工報告**：智能為您建議當日三大核心待辦（Top 3）。 |
| **`「今天寫得差不多了，收工！」`**<br>或 `「結束今天工作」` | **準備關電腦休息前** | 1. 背景自動進行代碼測試與 API 金鑰安全掃描。<br>2. 口頭確認完成的項目會自動在 `task.md` 中標註為 `[x]`。<br>3. 自動組裝符合規範的 Commit 訊息並進行本地提交與雲端推送（`git push`）。<br>4. 自動規劃出**「下一次開工應繼續的起點」**。 |

---

## 🧠 自動化運作機制
不論是本地還是雲端，AI 助理在收到引入指令後，都會自動識別該目錄下的 `SKILL.md` 索引，並將三大技能（`15-project-init`、`16-work-start`、`17-work-close`）自動加載至當前新專案的大腦記憶中。

---
*Created by Antigravity AI Code Companion © 2026. 祝您新專案開發順利！*
