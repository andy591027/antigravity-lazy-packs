# Antigravity 懶人包 #01：連接 Google NotebookLM

> 版本：v0.3（Antigravity 版、路徑與指令最佳化）
> 更新日期：2026-07-04
> 對應影片：Antigravity基本功 EP03

> 📌 **本懶人包可獨立執行**：會自動檢查並安裝所需工具，不需要先看過其他懶人包。你只要確認下方「先備條件」即可開始。

---

## 這個懶人包會幫你做什麼？

讓你的 Antigravity 能夠直接操控 Google NotebookLM，包括：
- 建立 notebook、上傳資料來源
- 產生教學簡報（Slide Deck）
- 產生資訊圖表（Infographic）
- 所有成品自動下載到電腦裡的指定資料夾

---

## 原理說明：這個懶人包在做什麼？

**關係圖**：

```
Antigravity ←(MCP 協定)→ notebooklm-mcp.exe (翻譯官) ←(Google 登入)→ NotebookLM
```

這個懶人包會在你的電腦裡裝一個叫 `notebooklm-mcp-cli` 的「翻譯官」，讓 AI agent 能透過它去操控 NotebookLM。

- **為什麼需要翻譯官？**
  NotebookLM 沒有官方 API，Google 沒開放程式直接呼叫。`notebooklm-mcp-cli` 是用「模擬瀏覽器操作」的方式，由 API 驅動網頁。

- **什麼是 MCP？**
  MCP（Model Context Protocol）是 AI agent 跟外部工具溝通的標準接口。只要工具支援 MCP，Antigravity 就能無縫串接。

- **為什麼要登入 Google？**
  `nlm` 需要你的 Google 通行證（Cookies），才能幫你去操作 NotebookLM。

**一句話記住**：你跟 Antigravity 講中文，Antigravity 叫 `notebooklm-mcp` 去幫你操作 NotebookLM，成品自動下載到你電腦的指定資料夾。

---

## 先備條件

在開始之前，請確認：

- [ ] Antigravity 已安裝且能正常使用
- [ ] 你有 Google 帳號（用來登入 NotebookLM）
- [ ] 電腦有網路連線

---

## 安裝與設定流程

### 步驟零：環境檢查

請 Antigravity 自動確認：
1. **確認作業系統**（Windows / macOS / Linux）
2. **檢查 Git 是否已安裝**：執行 `git --version`
3. **確認 Python 且 pip 可用**

---

### 步驟一：安裝 NotebookLM MCP CLI 工具

請使用 `pip` 或 `uv` 安裝 `notebooklm-mcp-cli`：

```powershell
pip install notebooklm-mcp-cli
```

安裝完成後，確認主要指令與路徑可用：

```powershell
nlm --version
where.exe notebooklm-mcp.exe
```

常見安裝路徑：
* `C:\Users\<你>\.local\bin\notebooklm-mcp.exe`
* `C:\Users\<你>\AppData\Local\Programs\Python\Python314\Scripts\notebooklm-mcp.exe`

---

### 步驟二：登入 Google 帳號

執行以下指令，會自動開啟瀏覽器讓您登入 Google：

```powershell
nlm login
```

> 🖐️ **需要手動操作**：瀏覽器會開啟 Google 登入頁面，請登入您的 Google 帳號。登入成功後，CLI 會自動擷取認證資訊。

登入成功後，確認認證與狀態：

```powershell
nlm doctor
```

確認結果顯示 `Cookies: present` 與登入之 Google 帳號（例如 `xxx@gmail.com`）。

---

### 步驟三：寫入 Antigravity MCP 設定

在 Antigravity 中，MCP 設定檔位於：

```text
C:\Users\<你>\.gemini\antigravity\mcp_config.json
```

請先備份：

```powershell
$config = "C:\Users\user\.gemini\antigravity\mcp_config.json"
$backup = "$config.bak-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
Copy-Item -LiteralPath $config -Destination $backup -Force
```

在 `mcpServers` 區塊中加入或修正 `notebooklm` 的設定：

```json
    "notebooklm": {
      "command": "C:\\Users\\user\\.local\\bin\\notebooklm-mcp.exe",
      "args": []
    }
```

> ⚠️ **重要路徑提醒**：
> * command 必須使用雙反斜線 `\\` 跳脫。
> * 請務必使用 `notebooklm-mcp.exe` 執行檔，而非 `nlm`（`nlm` 用於命令列管理，`notebooklm-mcp` 才是 MCP 伺服器主程式）。

---

### 步驟四：建立本地資料夾

請在文件下建立以下目錄結構，供下載成品儲存：

```
Documents/
  └── NotebookLM/
      ├── slides/          ← 簡報 (.pptx)
      ├── infographics/    ← 資訊圖表
      ├── audio/           ← 音訊概覽
      ├── video/           ← 影片概覽
      ├── docs/            ← Google 文件匯出
      ├── sheets/          ← Google 試算表匯出
      ├── mindmaps/        ← 心智圖
      └── quizzes/         ← 測驗與閃卡
```

---

### 步驟五：重啟 Antigravity 並驗證連接

請完全關閉 Antigravity 視窗或 IDE 並重啟，以使新的 MCP 設定生效。

重新開啟後，在對話中輸入：
```text
請列出我的 NotebookLM 筆記本清單。
```

若能成功顯示清單，代表連接完全成功！

---

## 常用控制指令 與 🇹🇼 強制繁體中文（zh-TW）生成規範

在預設狀態下，Google NotebookLM 生成素材時（尤其是簡報與資訊圖表）可能會預設使用英文。為了確保產出的所有成品均為**繁體中文（Traditional Chinese）**，我們必須在調用指令時明確指定 `--language zh-TW`，或在焦點（focus/prompt）中加入強制指令。

請參考以下常用控制指令對照表：

| 您說的話 | Antigravity 執行的背後指令 (強制繁體中文) | 存放位置 |
|----------|-------------------|---------|
| 「幫我用這份 PDF 建一個 notebook」 | `nlm notebook create --name "<名稱>"`<br>`nlm source create --file "<路徑>"` | — |
| 「幫我產生教學簡報」 | `nlm slides create <NOTEBOOK_ID> --language zh-TW` | slides/ |
| 「幫我做一張資訊圖表」 | `nlm infographic create <NOTEBOOK_ID> --language zh-TW` | infographics/ |
| 「幫我產生音訊概覽（Podcast）」 | `nlm audio create <NOTEBOOK_ID>` *(語音為英文，但可用 focus 引導簡介為中文)* | audio/ |
| 「幫我產生影片概覽」 | `nlm video create <NOTEBOOK_ID>` | video/ |
| 「幫我產生報告並匯出成文件」 | `nlm report create <NOTEBOOK_ID> --language zh-TW` | docs/ |
| 「幫我做數據表格並匯出試算表」 | `nlm data-table create <NOTEBOOK_ID> "<描述>" --language zh-TW` | sheets/ |
| 「幫我產生心智圖」 | `nlm mindmap create <NOTEBOOK_ID> --title "<中文標題>"` | mindmaps/ |
| 「幫我出測驗題 / 閃卡」 | `nlm quiz create <NOTEBOOK_ID> --focus "請全部使用繁體中文出題"`<br>`nlm flashcards create <NOTEBOOK_ID> --focus "請全部使用繁體中文製作"` | quizzes/ |

---

## 🤖 AI Agent (Antigravity) 專用語系與生成指令規範 (Agent Execution Instructions)

當 Antigravity 讀取此文件作為技能或指令指引時，必須嚴格遵守以下操作規範：

1. **強制繁體中文語系參數**：
   在呼叫 NotebookLM 相關 MCP 工具或 CLI 命令進行生成時，對於支援 `--language` 的生成任務，必須強制帶入 `--language zh-TW` 參數：
   - 產生簡報（Slide Deck）：`slides create ... --language zh-TW`
   - 產生資訊圖表（Infographic）：`infographic create ... --language zh-TW`
   - 產生報告（Report）：`report create ... --language zh-TW`
   - 產生數據表格（Data Table）：`data-table create ... --language zh-TW`

2. **引導與焦點指示（Focus & Prompt）**：
   對於不支援 `--language` 參數但支援 `--focus` 或 `--prompt` 的生成命令（例如 `quiz`、`flashcards`、`audio`、`video` 等），必須在參數中加上明確的中文指示，強制 NotebookLM 底層使用繁體中文生成。例如：
   - `quiz create ... --focus "請使用繁體中文（zh-TW）出題，切勿使用英文或簡體字。"`
   - `flashcards create ... --focus "請使用繁體中文（zh-TW）製作閃卡。"`

3. **雙重語系檢驗與修正**：
   - 如果下載回來的檔案內容為英文或簡體中文，Agent 必須主動使用 `revise`（例如 `slides revise`）或重新生成，並在修改指令中明確指出「請將以下內容全部翻譯並重寫為精美、專業的繁體中文（zh-TW）」。

---

## 踩坑與排查

| 狀況 | 原因 | 解法 |
|------|------|------|
| `No such command 'mcp'` | 使用了錯誤的 command 呼叫（如 `nlm mcp`） | 修正 command 為 `notebooklm-mcp.exe`，且不要在 `args` 傳入 `mcp` |
| 生成的簡報是英文版 | 未在指令中加上 `--language zh-TW` | 在 `nlm slides create` 時務必加上 `--language zh-TW` 參數 |
| 讀寫筆記本時失敗 | Google 登入 Cookie 過期或失效 | 重新執行 `nlm login`，並用 `nlm doctor` 驗證 |
| JSON 格式錯誤 | 修改 `mcp_config.json` 時漏了逗號或括號 | 驗證 `mcp_config.json` 格式，路徑反斜線須使用 `\\` 雙斜線 |
