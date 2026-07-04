# SOIL 三種簡報技能 — 給其他 Agent 讀取用

本資料夾收錄三種簡報生成技能,對應 AI Agent 時代的三種簡報路徑。
另一個 agent(GPT Codex / 其他 Claude session)可直接讀取本資料夾使用。

## 技能對照

| 資料夾 | 簡報類型 | 輸出 | 主要工具 |
|--------|----------|------|----------|
| `soil-image-deck/` | 純圖片簡報 | `.pptx`(每頁一張 AI 圖) | gpt-image-2 + python-pptx(`pack_pptx.py`) |
| `soil-teaching-deck/` | 圖 + 可編輯文字 | `.pptx`(文字物件可雙擊改) | gpt-image-2 + python-pptx |
| `soil-html-deck/` | HTML 簡報(自由度天花板) | 單一 `.html`(base64 內嵌圖) | gpt-image-2 + HTML/CSS/JS + Chart.js |

## 共同設計憲法

三種技能都遵守:
1. **林長揚 30 原則**(字級 55/34/21/13、Z 字排版、強調色 1-2 種、進度條、標題≤10 字…)
2. **SOIL 六引擎**:概念定位 → 脈絡定位 → 頁面架構 → 認知編修 → 風格建構 → 總導演
3. **SOIL 三段式脈絡**:引起動機 → 維持注意 → 喚起行動

每個 `SKILL.md` 內都有完整的執行流程、Prompt 範本、踩坑紀錄。

## 使用建議

- 收到使用者素材時,先讀對應 `SKILL.md` 的「執行流程」段
- 不要混用三種技能的輸出格式
- 圖像生成統一呼叫 `draw` 技能(gpt-image-2),預設 `--quality low`
- HTML 簡報的圖像**必須 base64 內嵌**,不可用相對路徑

## 同步來源

- 全域版本:`C:\Users\mathr\.claude-skills\soil-{image,teaching,html}-deck\`
- 本資料夾為**鏡像副本**,供其他 agent 讀取
