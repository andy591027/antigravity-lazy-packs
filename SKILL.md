---
name: antigravity-lazy-packs
description: Antigravity 懶人包全集 — 極致整合、MCP 連接、三大專屬高規自訂技能。當讀取「Antigravity 懶人包」時載入。
---

# Antigravity 懶人包 — AI 專屬自動化技能入口

當使用者提供此 repository 網址並希望在 Antigravity (Gemini) 環境中安裝自動化技能時，請依照本引導執行：

## 🚀 專屬高規自訂技能列表

此倉庫包含三大專屬客製化高規技能，完全支援 AI 大腦（如 Antigravity）直接讀取與運作：

| 編號 | Skill 名稱 | 功能說明 | 核心動作 |
|------|-----------|----------|----------|
| 01   | `15-project-init` | **專案初始化技能** | 1. 建立標準開發目錄（`src/`、`docs/`、`tests/`、`assets/`）<br>2. 自動生成 `.gitignore`、`README.md`、`AGENTS.md` 與 `task.md`<br>3. 執行 Git 初始化並完成首版提交。 |
| 02   | `16-work-start`   | **開工狀態檢查技能** | 1. 背景執行 `git pull` 同步最新進度防止衝突。<br>2. 智能分析 `task.md` 與大腦筆記，為您建議當日三大核心待辦（Top 3）。 |
| 03   | `17-work-close`   | **收工自動備份技能** | 1. 代碼測試與金鑰敏感度安檢。<br>2. 一鍵組裝 Conventional Commit 規範訊息並 `git push` 至雲端。<br>3. 自動標註完成任務並安排下次開工起點。 |
| 04   | `pdf-obsidian`     | **PDF-to-Obsidian 頂級結構化重構** | 1. 智慧自動分卷上傳與並行解析。<br>2. 資深技術文件結構化專家提示詞清洗，防呆扁平化複雜表格，消除空白欄位。<br>3. 自動首行 Frontmatter 對齊、警告 Callout 包裝與 Mermaid 流程圖生成。 |

---

## 🛠️ 安裝與調用指引

當您在對話中呼叫相關口令，Antigravity 會自動定位並讀取對應的 Skill 設定：

### 1. 🛠️ 專案初始化
- **口令**：`「準備開新專案」` 或 `「初始化專案」`
- **路徑**：[skills/15-project-init/SKILL.md](file:///skills/15-project-init/SKILL.md)

### 2. ☀️ 開工狀態檢查
- **口令**：`「開工！」` 或 `「準備開始工作」`
- **路徑**：[skills/16-work-start/SKILL.md](file:///skills/16-work-start/SKILL.md)

### 3. 🌙 收工自動備份
- **口令**：`「今天寫得差不多了，收工！」` 或 `「結束今天工作」`
- **路徑**：[skills/17-work-close/SKILL.md](file:///skills/17-work-close/SKILL.md)

### 4. 📚 PDF 轉 Obsidian 頂級智慧重構
- **口令**：`「解析 PDF」`、`「把 PDF 存到 Obsidian」` 或 `「讀取 PDF 筆記」`
- **路徑**：[skills/18-pdf-obsidian/SKILL.md](file:///skills/18-pdf-obsidian/SKILL.md)

---
*Created by Antigravity AI Code Companion © 2026.*
