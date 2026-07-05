---
name: pdf-obsidian
description: 讀取本地 PDF 檔案，將其以 Gemini 2.5 多模態原生模型分析，自動清洗並排版為高品質 Markdown 格式（含標題、表格、粗體，並可自動轉化關係圖為 Mermaid 流程圖），最後直接儲存至使用者指定的 Obsidian Vault 目錄。當使用者要求「解析 PDF」、「整理 PDF」、「把 PDF 存到 Obsidian」、「PDF 轉 Markdown」、「讀取 PDF 筆記」等任何將 PDF 轉化並匯入 Obsidian 知識庫的情境時，請調用此技能。
---

# PDF 轉 Obsidian 頂級自動化解析技能 (Gemini Multi-modal)

## 觸發情境
當使用者提到：
- 「幫我解析這個 PDF」、「整理這份 PDF 報告」
- 「把這篇 PDF 轉成 Markdown / 存到 Obsidian」
- 「這份 PDF 有什麼重點？幫我整理進 Obsidian」
- 「將 PDF 檔案轉換為精美筆記」等情境。

## 腳本位置
- Windows：`C:/Users/user/.gemini/config/plugins/pdf-obsidian-skill/skills/pdf_to_obsidian.py`
- macOS/Linux：`~/.gemini/config/plugins/pdf-obsidian-skill/skills/pdf_to_obsidian.py`

## 使用方式
```bash
python C:/Users/user/.gemini/config/plugins/pdf-obsidian-skill/skills/pdf_to_obsidian.py "D:/我的資料/report.pdf" --vault "C:/Users/Name/Documents/Obsidian/AI_Notes" --name "報告摘要"
```

### 參數
- `pdf_path`（必填）：PDF 檔案的絕對或相對路徑。
- `--vault`（選填）：您的 Obsidian Vault 或輸出資料夾路徑。若未填，預設會自動在當前專案下建立 `notes/` 資料夾。
- `--name`（選填）：輸出的 Markdown 檔名（不需要副檔名，預設自動使用 PDF 檔名或加上時間戳）。
- `--prompt`（選填）：可對 Gemini 增加客製化提問或重點提示（例如 "著重在財務報表與成本分析的部分"）。
- `--model`（選填）：預設使用極速划算的 `gemini-2.5-flash`。可選：`gemini-2.5-pro`。

## 核心映射與格式規範
為確保寫入 Obsidian 的筆記能立即享受到最 premium 的視覺效果，底層腳本整合了資深「技術文件結構化專家」黃金系統提示詞，具備以下卓越清洗能力：

1. **結構分明 (Hierarchy & Line-break)**：
   - 根據字體大小與章節編號，精準對應 `#`, `##`, `###`。
   - 自動修補 PDF 換行造成的強制斷行，整合語意為流暢段落。

2. **Frontmatter Line 1 完美對齊 (Line-1 Metadata Alignment)**：
   - 自動過濾並剔除 AI 生成時偶然帶有的廢話對話開場白與代碼包裹。
   - **強保 Markdown 檔案第一行 100% 開始於 `---` (YAML)**，符合 Obsidian 知識庫與 RAG 檢索的最高標準。
   - 多分卷並行提取時，自動擦除次要分卷重複的 Frontmatter。

3. **複雜表格防呆 (Flattening Complex Tables)**：
   - 針對合併儲存格等複雜表格，自動將其扁平化（Flatten）重構為高密度的無序清單或在子欄位中自動重複填入合併標題，**徹底消除空白欄位**，保障資訊零遺失。

4. **雜訊過濾與 Callout 包裝**：
   - 刪除純頁碼與無意義頁首尾，但將包含版本、日期的頁首尾自動提取至 Metadata。
   - 將「警告」、「注意」、「提示」自動轉換為標準 Markdown Callout（例如 `> ⚠️ **警告**：...`）。

5. **架構可視化 (Mermaid Diagrams)**：
   - 當偵測到組織架構、步驟流程、因果關係等，自動用 Mermaid 語法流程圖 / 關係圖（如 `graph TD`）將其可視化！
