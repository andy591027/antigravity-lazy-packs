# 懶人包 08：把 Google 經濟型生圖裝進 Antigravity

> 對應影片：**Antigravity 基本功 EP11 — 把 Google 經濟型生圖裝進 Antigravity**
> 目標：五分鐘內完成安裝，讓 Antigravity 能夠用最便宜、甚至免費的方式生圖！
> 費用：
> - **`low` 等級（極力推薦）**：使用 Google 最新推出的 **`gemini-2.5-flash-image`**，在 Google AI Studio 享有 **100% 免費額度（Free Tier）**！
> - **`medium` 等級**：使用 **`imagen-4.0-fast-generate-001`**（極速省電型），每張圖僅約 **NT$0.06**，CP值極高！

---

## 你會得到什麼

裝好後，在 **任何** 專案資料夾裡對 Antigravity 說：

> 「畫一隻穿西裝的龍蝦，扁平向量插畫風格」

Antigravity 會自動呼叫超便宜的 **`gemini-2.5-flash-image`**（預設為 `low` 等級）生圖，存到當前資料夾的 `slides/generated/`（或 `./generated/`）裡。

---

## 你需要手動準備的兩件事

Antigravity 沒辦法幫你做這兩件事（需要本人身份驗證）。做完之後把剩下的全部交給 Antigravity。

### ① 取得 Google AI Studio API Key

1. 到 [aistudio.google.com](https://aistudio.google.com)，用你的 Google 帳號登入
2. 點擊 **Get API key** → **Create API key**
3. 選擇你的專案並 **複製那串 `AIzaSy...` 開頭的 Key**
4. 暫時貼到記事本

### ② 儲存 API Key 到全域環境

將你的 API Key 寫入使用者 Home 目錄下的 `.gemini.env`（**全域可用**，任何專案都吃得到）：

```
GEMINI_API_KEY=AIzaSy使用者貼的那串
```

- Windows 路徑：`C:/Users/<使用者>/.gemini.env`
- macOS/Linux：`~/.gemini.env`

---

# 🤖 Antigravity 執行區（以下由 AI 自動完成）

您是 Antigravity 助手。此技能已由系統自動為您安裝並配置完成。

## 任務 1：建立全域 draw Skill

配置全域外掛與技能目錄：
- Windows：`C:/Users/user/.gemini/config/plugins/draw-skill/`
- macOS/Linux：`~/.gemini/config/plugins/draw-skill/`

此目錄下包含三個檔案：
1. `plugin.json`：外掛設定描述
2. `skills/draw.py`：核心生圖 Python 腳本（支援 CLI 命令行與 native 技能函數）
3. `SKILL.md`：Antigravity 技能調用規則手冊

---

## 核心生圖腳本介紹：`draw.py`

此腳本整合了 **雙重 Google 生成 API**，會根據您的需求，自動切換至最划算的模型。

### 支援的三大畫質等級（自動對應最實惠的模型）：
- **`low`**（預設，**100% 免費 / 極低成本**）：對應 **`gemini-2.5-flash-image`**（Google 最新原生的超快速生圖模型，在 AI Studio 享有免费額度，日常草稿與 99% 的簡報插圖首選！）。
- **`medium`**（約 NT$0.06）：對應 **`imagen-4.0-fast-generate-001`**（最新 Imagen 4 快速型，速度快，細節與色彩出眾，CP值極高！）。
- **`high`**（約 NT$0.12）：對應 **`imagen-4.0-generate-001`**（最新 Imagen 4 標準型，適合封面及需要極致畫質的場合）。

---

## 驗證安裝與測試生圖

在終端機中執行下列指令測試生成一張黑貓插畫：

```bash
python C:/Users/user/.gemini/config/plugins/draw-skill/skills/draw.py "一隻可愛的黑貓，扁平插畫風格" --name test
```

### 預期結果：
- 終端機顯示 `[OK] .../generated/test_<時間戳>.png`
- 開啟該檔案能看到滿版黑貓插畫！

---

## 🎉 安裝完成！

以後在任何專案裡，直接對我說「**畫一張 XX**」或「**生一張 XX 的圖**」，我就能呼叫 Google 生圖模型為您完美生圖！

- **預設目錄**：自動建立並存放在專案底下的 `slides/generated/` 或 `./generated/`
- **完美相容**：完美相容 SOIL 簡報引擎（如 `soil-image-deck`）的 `--quality` 與寬高規格（自動將寬高如 `1536x1024` 映射為 Google `16:9` 滿版底圖）！
- **極致美學**：支援多種長寬比（`1:1`、`16:9`、`9:16`、`4:3`、`3:4`）。
