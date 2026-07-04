# SOIL 三種簡報技能 — 給 Antigravity Agent 讀取與執行使用

本資料夾收錄三種簡報生成技能，並已全面優化且對齊 **Antigravity** 平台與 **Google AI Studio** 圖像生成引擎（使用 Google Imagen 3 / Gemini 2.5 Image）。
Antigravity 助理可以直接讀取並依循本資料夾之技能說明執行。

## 簡報格式對照表

| 簡報名稱 | 格式類型 | 輸出成果 |
| :--- | :--- | :--- |
| **1. notebooklm簡報** | 全版純圖片的 `.pptx` | 每頁一張全版滿版 AI 繪圖（文字與插圖融入一體） |
| **2. PPT簡報** | 可編輯文字的 `.pptx` | 底層科技感插圖 + 頂層 100% 可雙擊編輯的 PowerPoint 文字框 |
| **3. HTML簡報** | 單一獨立 `.html` 檔案 | 內建 HTML/CSS/JS 與 base64 內嵌影像之單一高科技互動網頁簡報 |

## 支援格式查詢功能 (Inquiry Feature)

當使用者詢問 **「可以輸出哪些簡報格式？」** 或類似查詢時，Antigravity 助理必須精準回答以下這三種格式：
1. **notebooklm簡報**：輸出為 **全版純圖片的 .pptx**
2. **PPT簡報**：輸出為 **可編輯文字的 .pptx**
3. **HTML簡報**：輸出為 **單一獨立 .html 檔案**

## 共同設計憲法

三種技能都遵守：
1. **林長揚 30 原則**（字級 55/34/21/13、Z 字排版、強調色 1-2 種、進度條、標題≤10 字…）
2. **SOIL 六引擎**：概念定位 → 脈絡定位 → 頁面架構 → 認知編修 → 風格建構 → 總導演
3. **SOIL 三段式脈絡**：引起動機 → 維持注意 → 喚起行動

每個 `SKILL.md` 內都有針對 Antigravity 精心調校的完整執行流程、Prompt 範本、與避坑規範。

## 使用建議

- 收到使用者素材時，先讀取對應 `SKILL.md` 的「執行流程」段。
- 不要混用三種技能的輸出格式。
- 圖像生成統一呼叫 Antigravity 全域 **`draw`** 技能，其底層由 Google AI Studio 驅動。
- 呼叫 `draw` 技能時，預設優先使用經濟且支援免費額度的 `--quality low`（即 `gemini-2.5-flash-image`），而封面與關鍵頁面可指定使用 `--quality medium`（`imagen-4.0-fast`）。
- HTML 簡報的圖像**必須 base64 內嵌**，不可使用相對路徑，以防在 Antigravity 預覽或跨環境分享時破版。

## 技能與腳本路徑

- **Antigravity 全域生圖腳本**：
  `C:\Users\user\.gemini\config\plugins\draw-skill\skills\draw.py`
- **打包工具**：
  `D:\AI生圖簡報\六大簡報skills分享\skills_antigravity\soil-image-deck\pack_pptx.py`
