---
name: project-init-sync
description: 專案初始化技能。說「開新專案」「初始化專案」「15-project-init」時載入，自動建立標準專案結構與核心管理檔案。
---

# 專案初始化技能 (Project Init Sync)

當使用者要求「初始化新專案」或「開新專案」時，AI Agent 應依序執行以下步驟：

## 步驟一：收集專案基礎資訊
主動問使用者：
1. **專案名稱** 與 **用途簡述**。
2. **開發語言 / 技術棧**（例如 Node.js, Python, HTML/CSS）。
3. 是否需要建立關聯的 **GitHub Repository** (及公開或私有)。

## 步驟二：建立標準目錄結構
根據技術棧建立對應目錄：
* 通用：`src/` (原始碼), `docs/` (文件), `tests/` (測試), `assets/` (資產)

## 步驟三：生成核心專案設定與管理檔案
1. **`README.md`**：包含專案名稱、簡介、安裝方法與執行說明。
2. **`.gitignore`**：忽略本地臨時檔、環境變數與 `node_modules/`。
3. **`AGENTS.md`**：專門給其他協作 AI Agent 閱讀的引導檔案，定義專案架構、開發規範與核心任務。
4. **`task.md`**：TODO 任務清單，列出初期開發任務。

## 步驟四：初始化 Git 儲存庫
在專案根目錄執行：
```powershell
git init
git add .
git commit -m "chore: initial project structure"
```
（若使用者要求且已登入 GitHub CLI，則執行 `gh repo create` 建立遠端儲存庫並關聯）

## 步驟五：回報初始化成果
以 Markdown 條列展示建立的目錄與檔案結構，並提示使用者隨時可以執行「開工技能」開始開發。
