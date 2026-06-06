# Antigravity 懶人包全集 — 連接與極致整合指南 (NotebookLM, GitHub, 自訂技能與原生生圖)

> 版本：v1.0（Antigravity 專屬版）
> 更新日期：2026-06-06

> ✅ 本倉庫專為 Google DeepMind 開發之 **Antigravity (Gemini) AI 協作大腦** 量身打造；完美整合全方位 CLI、MCP 協定、本地高效工作流以及內建優勢。

---

## 🛠️ 這個懶人包會幫你做什麼？

引導您在 Antigravity 系統中快速對接並啟用今日所有最頂尖的開發與大腦整合服務：
- **連接 Google NotebookLM**：安裝、驗證與配置 `notebooklm-mcp-cli`，直接與您的線上記事本筆記與 sources 對談。
- **連接 GitHub**：快速對接 GitHub API、檢查登入狀態與排除 GITHUB_TOKEN 的權限衝突。
- **建置三大高效率工作流自訂技能**：
  1. 🛠️ **專案初始化 (`15-project-init`)**：一鍵建立標準目錄結構、`AGENTS.md`、`task.md`。
  2. ☀️ **開工技能 (`16-work-start`)**：自動檢查 Git 狀態、同步雲端、喚醒任務並條列今日待辦。
  3. 🌙 **收工技能 (`17-work-close`)**：自動安檢、一鍵 Conventional Commit 本地提交、推送備份至雲端並登錄 TODO 進度。
- **極致繁體中文原生生圖與繪製**：完全捨棄第三方 plugins，直接調用 Antigravity 內建高規 `generate_image` 生圖工具與 Python Pillow 向量中文折行引擎，在指定資料夾生成印刷級繁體中文資訊圖表。

---

## 📂 倉庫檔案結構

本 Repo 包含了精簡的 Antigravity 懶人包核心檔案與成果展示：
- [README.md](README.md) — 本導讀文件與整合指引。
- [10-連接-Antigravity-極致整合懶人包.md](10-連接-Antigravity-極致整合懶人包.md) — 專門為別的使用者設計的「一鍵讀取」懶人包 MD 導讀檔案。
- [SKILL.md](SKILL.md) — 專屬自訂技能的主入口註冊檔。
- `skills/` — 三大自動化高規自訂技能目錄。
  - `skills/15-project-init/SKILL.md` — 專案初始化技能。
  - `skills/16-work-start/SKILL.md` — 開工技能。
  - `skills/17-work-close/SKILL.md` — 收工技能。
- 🎨 **視覺與互動式資訊圖表展示**：
  - [ai_agent_era_concept.png](ai_agent_era_concept.png) — 科技暗色調人機協作概念背景圖。
  - [infographic_ai_agent_era.png](infographic_ai_agent_era.png) — 本地 Python (Pillow) 向量繪圖程式結合微軟正黑體生成的排版資訊圖表。
  - [infographic_ai_agent_era.html](infographic_ai_agent_era.html) — 響應式毛玻璃擬態（Glassmorphic UI）動態資訊圖表網頁。

---

## ⚙️ 先備條件

- [ ] Google 帳戶（已登入 NotebookLM，並有可用的記事本）
- [ ] Windows / macOS 開發環境，且已安裝 Node.js (v18+)、Git、GitHub CLI、uv

---

## 🚀 使用指引與步驟

### 步驟一：設定 Google NotebookLM 連接
1. **安裝 CLI 工具**：
   ```powershell
   uv tool install notebooklm-mcp-cli
   ```
2. 🖐️ **手動登入 NotebookLM**：
   在終端機執行 `nlm login`，完成後關閉自動拉起的瀏覽器。
3. **終端機驗證**：
   執行 `nlm list notebooks` 列出您的記事本，確認中文無虞。
4. **對接 Antigravity MCP 設定**：
   請 Antigravity 將 NotebookLM MCP 寫入您的全域 MCP 設定檔 `C:\Users\user\.gemini\antigravity\mcp_config.json`：
   ```json
   "notebooklm": {
     "command": "nlm",
     "args": ["mcp", "start"]
   }
   ```

### 步驟二：對接 GitHub 帳戶
1. **檢查登入狀態**：
   執行 `gh auth status`。
2. **解決 token 遮蔽衝突**：
   若環境中存在無效的 `GITHUB_TOKEN`，執行：
   ```powershell
   # Windows PowerShell 排除法
   $env:GITHUB_TOKEN = $null; gh auth status
   ```

### 步驟三：呼叫三大高效自訂技能
本專案已在 `skills/` 目錄下部署了三大全自動化技能，Antigravity 會在您下達對應口令時自動讀取執行：
- 🛠️ **專案初始化**：呼叫 `「準備開新專案」` 或 `「初始化專案」`。
- ☀️ **開工狀態檢查**：呼叫 `「開工！」` 或 `「準備開始工作」`。
- 🌙 **收工自動備份**：呼叫 `「今天寫得差不多了，收工！」` 或 `「結束今天工作」`。

### 步驟四：使用原生高質感繁體中文生圖
直接在 Antigravity 系統中要求：
> *「幫我針對最近這本 NotebookLM 的內容，繪製一張繁體中文高解析度的資訊圖表」*
Antigravity 會自動調用 `generate_image` 生圖，並於背景結合 Windows 的「微軟正黑體」字型 (`C:\Windows\Fonts\msjh.ttc`) 與 Python Pillow 向量運算程式，生成完美的 `infographic_ai_agent_era.png` 中文圖表！

---
*Created by Antigravity AI Code Companion © 2026.*
