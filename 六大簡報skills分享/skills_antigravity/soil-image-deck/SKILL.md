---
name: soil-image-deck
description: >
  SOIL 純圖片教學簡報技能（又名 notebooklm簡報）。遵循 SOIL Teaching Deck Workflow 六顆引擎的教學設計邏輯，
  但每一頁都是由 Antigravity 全域 draw 技能完整生成的 PNG 圖片（包含標題、內文、視覺），
  最後打包成全版純圖片的 .pptx。
  當使用者說「做純圖片簡報」、「notebooklm簡報」、「全圖簡報」、「每頁都是 AI 生的圖」、
  「做一份全版純圖片的 pptx 簡報」、「快速做一份視覺震撼的簡報」等需求時，
  請一定要使用此技能。
  本技能與 soil-teaching-deck 不同：soil-teaching-deck 產出「文字可編輯 + AI 插圖」的
  混合簡報；本技能產出「每頁都是單張 AI 圖」的純圖片簡報，適合
  快速產出、社群貼文、視覺強烈的開場、或不需後續文字編輯的場合。
---

# SOIL 純圖片教學簡報（soil-image-deck - Antigravity 版）

以 SOIL 六顆引擎的教學判斷為骨架，用 Antigravity `draw` 技能逐頁生成**整頁圖像**，最後打包成 .pptx。

> **與 soil-teaching-deck 的差別**
> - `soil-teaching-deck`：產出「可編輯文字 + 插圖」的 editable pptx
> - `soil-image-deck`（本技能）：引擎六生成整頁圖（或整頁背景），打包成 pptx（每頁就是一張 full-bleed 圖）

---

## 適用情境

| 情境 | 為什麼用本技能 |
|------|----------------|
| 直播開場、研習暖場 | 要視覺衝擊，不需要台下帶回去編輯 |
| 社群分享、FB / IG 貼文 | 每張圖就是一則獨立素材 |
| 快速原型、腦力激盪 | 快速出 10 張，不糾結排版 |
| YouTube 影片章節過場 | 風格統一、節奏清楚 |
| 節慶／宣傳海報簡報 | 圖像為主、文字為輔 |

---

## 第一步：判斷工作模式

**問使用者（只問這一題）：**

> 請問你目前的狀況是？
> 1. 我有素材（文字、教材、腳本），想做成純圖片簡報
> 2. 我只有一個主題或一句話，想從頭開始
> 3. 我有現成的 YAML 規格，直接跑生圖與打包

| 回答 | 跑哪幾顆引擎 |
|-----|--------------|
| 1 | 引擎 1→2→3→4→5→6 |
| 2 | 先協助擴充內容 → 引擎 1→2→3→4→5→6 |
| 3 | 跳過引擎 1–5，直接進入引擎 6（I-1 批次生圖 → I-2 QA → I-3 打包）|

---

## 第二步：進入引擎前補問

### 進引擎一前補問：
> 1. **教學對象是誰？**（國中生、高中生、老師研習、一般觀眾、社群受眾）
> 2. **簡報總頁數？**（預設 10 頁；社群貼文通常 6–9 頁）
> 3. **預估生圖成本**（Low 品質對應 `gemini-2.5-flash-image` 可享用免費額度；Medium 品質對應超值 `imagen-4.0-fast`，成本極低）

### 進引擎五前補問：
> 1. **有偏好的視覺風格嗎？**（例如：扁平插畫、手繪粉筆風、新聞風、科技感、水彩）
> 2. **主要色系？**（例如：深藍 + 金黃、米色 + 墨綠）

---

## 引擎三：頁面架構師

每頁指定角色後，本技能額外產出「**image brief**」，作為引擎六生圖的基礎。

### 每頁要指定
- 頁碼
- 頁面角色（封面／問題引入／迷思澄清／比較／流程／分類／案例／數據／總結／行動／過渡）
- 本頁主重點（一句話）
- **on-image text**：圖上要出現的文字（建議中文字 $\le$ 20 字）
- **image_brief**：這張圖的核心構圖（主角、場景、動作、象徵物）
- **layout_hint**：版面佈局（置中大標、左文右圖、全版背景等）

### 輸出格式

```yaml
pages:
  - page: 1
    role: 封面
    core_point: "把 Google 生圖整合進 Antigravity"
    on_image_text:
      title: "把 Google 生圖整合進 Antigravity"
      subtitle: "draw 技能 × SOIL 簡報工作流"
    image_brief: "Q版機器人老師站在發光黑板前手持畫筆，黑板上有電路與公式圖案"
    layout_hint: "左文右圖；標題置左上 1/3，圖像置右 2/3"
```

---

## 引擎五：風格建構師（產出 image_policy）

```yaml
image_policy:
  # 風格描述（會串接進每張生圖 prompt）
  style_tokens: "扁平向量插畫、16:9橫版、深夜藍#0D1B2A背景、亮青藍#00C6FF主色、金黃#FFD700點綴、現代教育科技風"
  negative: "不要逼真照片、不要雜亂背景、不要英文字、不要亂碼"
  size: "1536x1024"            # 自動映射至 16:9 比例
  quality: "low"               # 預設 low (對應 gemini-2.5-flash-image 經濟免費版)
  font_feel: "粗體無襯線、標題大字"
```

---

## 引擎六：簡報總導演（純圖片版）

### 生成流程（三階段：I-1 → I-2 → I-3）

#### I-1：批次生圖
合併風格與各頁規格，呼叫 Antigravity 全域 **`draw`** 技能：

```bash
# 預設呼叫
python C:/Users/user/.gemini/config/plugins/draw-skill/skills/draw.py "{layout_hint}。圖像內容：{image_brief}。風格：{style_tokens}" --size 1536x1024 --quality low --name page_01 --outdir generated/
```

#### I-2：視覺確認（必做）
逐張確認是否有生圖錯字、亂碼、或風格偏離。不合格的單頁調整 prompt 重新生成。

#### I-3：打包成 PPTX
使用隨附的打包腳本 `pack_pptx.py`：

```bash
python D:/AI生圖簡報/六大簡報skills分享/skills_antigravity/soil-image-deck/pack_pptx.py \
  --images-dir generated \
  --output D:/AI生圖簡報/我的簡報.pptx \
  --title "簡報標題"
```

---

## 模式選擇：baked vs plate

| 模式 | 圖內是否含文字 | 文字是否可編輯 | 打包參數 |
|------|--------------|--------------|------------|
| `baked`（預設） | ✅ 文字由 AI 直接生成在圖裡 | ❌ 不可編輯 | `--mode baked` |
| `plate` | ❌ 純插畫設計底圖、無任何文字 | ✅ 文字是 pptx 動態疊加文字框 | `--mode plate --spec spec.yaml` |

### plate 模式下的 spec.yaml 格式範例：

```yaml
style:
  palette:
    bg: "#0D1B2A"
    primary: "#00C6FF"
    highlight: "#FFD700"
    text: "#FFFFFF"
    muted: "#A5B4CB"
  font: "Microsoft JhengHei"

pages:
  - page: 1
    image: page_01           # 自動對齊 images 內最新生成之 page_01_*.png
    img_x: 0
    img_y: 0
    img_w: 13.333
    img_h: 7.5
    blocks:
      - type: title          # 大標題
        text: "生圖整合\n進 Antigravity"
        x: 0.7
        y: 1.6
        w: 6.5
        h: 2.5
        size: 48
        color: text
        bold: true
```

* 可用的 block type：`title` / `subtitle` / `body` / `muted` / `highlight` / `badge` / `card` / `bar` / `progress` (進度條)
* 字級預設遵循林長揚文字階層。

---

## 依賴需求

- `draw` 技能（路徑：`C:/Users/user/.gemini/config/plugins/draw-skill/skills/draw.py`）
- 本地打包工具 `pack_pptx.py`（與本檔案同目錄）
- 環境需安裝 `python-pptx`、`Pillow`、`openai`
- 透過 `GEMINI_API_KEY` 環境變數對接 Google AI Studio。
