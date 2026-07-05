"""
Antigravity PDF-to-Obsidian 全域解析與清洗腳本

用法：
  python pdf_to_obsidian.py "D:/Documents/report.pdf" --vault "C:/Users/Name/Documents/Obsidian/AI_Notes" --name "報告摘要"

會自動讀取環境變數中的 GEMINI_API_KEY。
"""

import os
import sys
import argparse
import time
import shutil
import tempfile
from pathlib import Path
from datetime import datetime

# 強制將 Windows 終端機 stdout / stderr 設為 UTF-8 編碼，防止 print 含有中文字串時發生 UnicodeEncodeError
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# 預設參數
DEFAULT_MODEL = "gemini-2.5-flash"


def load_env_from_file(path: Path):
    if not path.exists():
        return
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    except Exception as e:
        print(f"警告：讀取環境變數檔案 {path} 失敗：{e}", file=sys.stderr)


def load_env():
    load_env_from_file(Path.cwd() / ".env")
    load_env_from_file(Path.home() / ".gemini.env")


def strip_frontmatter(text: str) -> str:
    text = text.strip()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text


def clean_markdown_code_block(text: str) -> str:
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[11:].strip()
    elif text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text


def perfect_frontmatter_alignment(content: str) -> str:
    content = content.strip()
    import re
    
    # 1. 尋找是否含有 ```yaml ... ``` 區塊，若有則直接提取
    yaml_pattern = re.compile(r"```yaml\s*([\s\S]*?)\s*```")
    match = yaml_pattern.search(content)
    
    if match:
        yaml_body = match.group(1).strip()
        post_content = content[match.end():].strip()
        # 如果 post_content 開頭依然含有多餘的 ---，予以清除
        if post_content.startswith("---"):
            parts = post_content.split("---", 2)
            if len(parts) >= 3:
                post_content = parts[2].strip()
            elif len(parts) == 2:
                post_content = parts[1].strip()
        return f"---\n{yaml_body}\n---\n\n{post_content}"
        
    # 2. 如果沒有 ```yaml 而是標準的 --- 包裹，但前面可能被加上了開場白
    if "---" in content:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front_body = parts[1].strip()
            # 確保 front_body 內沒有殘留的 ```yaml 或 ```
            front_body = front_body.replace("```yaml", "").replace("```", "").strip()
            post_content = parts[2].strip()
            return f"---\n{front_body}\n---\n\n{post_content}"
            
    return content


def resolve_outdir(vault_dir: str, pdf_path: Path) -> Path:
    if vault_dir:
        return Path(vault_dir)
    # 預設存放在當前工作目錄的 notes 目錄
    return Path.cwd() / "notes"


SYSTEM_INSTRUCTION = """
# Role
你是一位資深的「技術文件結構化專家」，精通 Markdown 語法、資訊架構與 RAG 知識庫前處理。你的任務是讀取我提供的 PDF 檔案，並將其完美還原為結構清晰的 Markdown 格式，以便後續匯入 Obsidian 作為知識庫使用。

# Task
將提供的 PDF 內容轉換為 Markdown (.md) 格式，確保標題層級正確、段落通順、複雜資料得以妥善重構，並在檔案開頭建立檢索用的 Metadata。

# Guidelines

## 1. 建立後設資料 (Frontmatter)
- 在輸出的 Markdown 最頂端，必須包含 YAML 格式的 Frontmatter。
- 請從文件中提取資訊，包含：`title:`（文件名稱）、`type:`（如 SOP、說明書、規格表）、`version:`（若有修訂版本號/日期請保留，若無則留空）、`summary:`（用一句話總結此文件核心）。

## 2. 標題層級與段落重塑 (Hierarchy & Line-break)
- 判斷字體大小與章節編號，精準對應 `#`, `##`, `###`。嚴禁將普通段落加上標題標籤。
- 修復因 PDF 排版造成的強制斷行，將語意接合為通順段落。段落間保留一個空行。

## 3. 雜訊過濾與重要標示 (Noise & Callouts)
- 刪除純粹的頁碼與無意義的頁首/頁尾。**但若頁首/頁尾包含「修訂日期、版本號、機密等級」，請將其提取至 Frontmatter 中。**
- 原文中的「警告 (Warning)」、「注意 (Note)」、「提示 (Tip)」區塊，請使用 Markdown 引用語法包裝（例如：`> ⚠️ **警告**：...`），以區隔於一般正文。

## 4. 表格與複雜數據重構 (Tables Handling)
- 標準表格：使用標準 Markdown 表格語法重建，確保對齊，並合併跨頁的同一表格。
- **複雜表格（合併儲存格）防呆**：Markdown 不支援合併儲存格。若遇到這類表格，請將其「扁平化」轉換為結構化的無序清單，或將合併的標題重複填入每個子欄位中，確保資訊關聯性不遺失。

## 5. 圖片與程式碼區塊 (Images & Code)
- 圖片請替換為 `[圖片說明：根據上下文推測圖片顯示內容]`。
- 程式碼、系統變數名稱、指令，使用反引號（` ` `）包裝。

# Output Format
- 只需輸出轉換後的 Markdown 內容（包含頂端的 YAML），不需要任何開場白或解釋。
- 確保輸出結果可以直接存成 .md 檔案並完美渲染。
"""


def convert_pdf_to_obsidian(pdf_path: str, vault_dir: str = None, name: str = None, custom_prompt: str = None, model_name: str = DEFAULT_MODEL) -> str:
    """
    將本地 PDF 檔案上傳至 Google AI Studio，利用 Gemini 2.5 進行多模態提取、Markdown 格式化，並寫入 Obsidian。
    """
    load_env()
    
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "錯誤：找不到 GEMINI_API_KEY 或 GOOGLE_API_KEY 環境變數，請在 ~/.gemini.env 中設定您的 API key。"
        
    p_path = Path(pdf_path)
    if not p_path.exists():
        return f"錯誤：找不到指定的 PDF 檔案：{pdf_path}"
        
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        return "錯誤：未安裝 'google-genai' 套件，請執行 'pip install google-genai' 安裝。"
        
    outdir = resolve_outdir(vault_dir, p_path)
    outdir.mkdir(parents=True, exist_ok=True)
    
    # 決定輸出檔名
    if name:
        out_filename = f"{name}.md" if not name.endswith(".md") else name
    else:
        out_filename = f"{p_path.stem}_Notes.md"
        
    out_file_path = outdir / out_filename
    
    print(f"正在連線 Google AI Studio (模型: {model_name})...")
    client = genai.Client(api_key=api_key)
    
    # 讀取 PDF 頁數與分割邏輯
    try:
        import pypdf
    except ImportError:
        import subprocess
        print("正在背景自動安裝 pdf 處理套件 pypdf...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
        import pypdf

    try:
        reader = pypdf.PdfReader(p_path)
        total_pages = len(reader.pages)
        print(f"PDF 檔案資訊：共 {total_pages} 頁，大小為 {p_path.stat().st_size / 1024 / 1024:.2f} MB")
    except Exception as pdf_read_err:
        return f"錯誤：無法使用 pypdf 讀取 PDF 檔案資訊：{pdf_read_err}"

    MAX_PAGES_LIMIT = 250
    chunks = []
    
    # 決定分卷
    if total_pages <= MAX_PAGES_LIMIT:
        print(f"頁數 {total_pages} <= {MAX_PAGES_LIMIT}，無需分卷處理，直接整卷解析。")
        chunks.append((p_path, 0, total_pages))
    else:
        print(f"偵測到大頁數 PDF ({total_pages} 頁 > {MAX_PAGES_LIMIT} 頁限制)，啟動「自動智慧分卷」排版技術...")
        for start in range(0, total_pages, MAX_PAGES_LIMIT):
            end = min(start + MAX_PAGES_LIMIT, total_pages)
            writer = pypdf.PdfWriter()
            for page_num in range(start, end):
                writer.add_page(reader.pages[page_num])
            
            temp_dir = Path(tempfile.gettempdir())
            chunk_path = temp_dir / f"pdf_chunk_{start + 1}_{end}_{int(time.time())}.pdf"
            with open(chunk_path, "wb") as f:
                writer.write(f)
            chunks.append((chunk_path, start, end))
        print(f"成功將文件分割成 {len(chunks)} 個分卷進行深度分步解析。")

    local_temp_files_to_clean = []
    for chunk_path, start, end in chunks:
        if chunk_path != p_path:
            local_temp_files_to_clean.append(chunk_path)

    combined_markdown = []
    
    try:
        for idx, (chunk_path, start, end) in enumerate(chunks):
            chunk_label = f"分卷 {idx + 1}/{len(chunks)} (第 {start + 1} 頁至第 {end} 頁)"
            print(f"\n──────────────────────────────────────────────────────────")
            print(f"正在處理：{chunk_label}")
            print(f"──────────────────────────────────────────────────────────")
            
            # 對 chunk_path 進行非 ASCII 字元相容檔名轉換
            temp_upload_path = None
            try:
                chunk_path.name.encode('ascii')
                upload_path = chunk_path
            except UnicodeEncodeError:
                temp_dir = Path(tempfile.gettempdir())
                temp_upload_path = temp_dir / f"gemini_chunk_{start}_{end}_{int(time.time())}.pdf"
                shutil.copy2(chunk_path, temp_upload_path)
                upload_path = temp_upload_path
                local_temp_files_to_clean.append(temp_upload_path)
                
            print(f"正在讀取並上傳檔案資訊: {upload_path.name} ({upload_path.stat().st_size / 1024 / 1024:.2f} MB)...")
            uploaded_file = client.files.upload(file=upload_path)
            print(f"上傳成功！檔案 ID: {uploaded_file.name}")
            
            # 等待檔案處理
            print("等待 Google 進行多模態排版預處理...", end="", flush=True)
            while uploaded_file.state.name == "PROCESSING":
                print(".", end="", flush=True)
                time.sleep(2)
                uploaded_file = client.files.get(name=uploaded_file.name)
            print()
            
            if uploaded_file.state.name == "FAILED":
                return f"錯誤：Google API 在預處理 {chunk_label} 時失敗。"
                
            print(f"預處理完成！正在提取、重排與清洗 {chunk_label} 的內容...")
            
            # 組合 prompt
            base_prompt = f"請詳細閱讀這份 PDF 檔案的第 {start + 1} 頁至第 {end} 頁，提取核心概念、核心架構、關鍵細節與表格，並根據系統指令將其轉換為最頂級精緻的 Obsidian 筆記章節。請確保內容的深度與覆蓋面，不要遺漏任何重要細節。"
            if custom_prompt:
                base_prompt += f"\n\n【使用者特別要求指定重點】：\n{custom_prompt}"
                
            # 呼叫 generate_content
            response = client.models.generate_content(
                model=model_name,
                contents=[uploaded_file, base_prompt],
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    response_mime_type="text/plain",
                    temperature=0.2,
                )
            )
            
            markdown_text = response.text
            if not markdown_text:
                return f"錯誤：模型在解析 {chunk_label} 時未返回任何內容。"
                
            # 儲存
            cleaned_md = clean_markdown_code_block(markdown_text)
            combined_markdown.append(cleaned_md)
            
            # 嘗試刪除 Google AI Studio 暫存檔案
            try:
                client.files.delete(name=uploaded_file.name)
                print(f"已成功清除 Google 暫存檔案：{uploaded_file.name}")
            except Exception as delete_error:
                pass
                
            # 提前刪除該輪臨時 upload_path
            if temp_upload_path and temp_upload_path.exists():
                try:
                    temp_upload_path.unlink()
                    local_temp_files_to_clean.remove(temp_upload_path)
                except Exception:
                    pass
                    
        # 寫入目標檔案
        processed_chunks = []
        for idx, (chunk_path, start, end) in enumerate(chunks):
            md_text = combined_markdown[idx]
            chunk_label = f"分卷 {idx + 1}/{len(chunks)} (第 {start + 1} 頁至第 {end} to 頁)"
            # Note: There was a typo in 'end to 頁' in index label but we use {end} 頁
            chunk_label = f"分卷 {idx + 1}/{len(chunks)} (第 {start + 1} 頁至第 {end} 頁)"
            if idx == 0:
                # 保持原樣（最頂端為 YAML frontmatter）
                processed_chunks.append(md_text)
            else:
                # 移除次要分卷的 frontmatter，並加上小章節分界標題
                clean_md = strip_frontmatter(md_text)
                part_title = f"## 📖 導讀章節：{chunk_label}\n\n"
                processed_chunks.append(part_title + clean_md)
                
        final_markdown = "\n\n---\n\n".join(processed_chunks)
        final_markdown = perfect_frontmatter_alignment(final_markdown)
        out_file_path.write_text(final_markdown, encoding="utf-8")
        
        return f"Successfully generated split Obsidian note! Saved to: {out_file_path.resolve()}"
        
    except Exception as e:
        return f"執行過程中發生錯誤：{str(e)}"
    finally:
        # 清理所有剩餘的本地臨時副本
        for temp_file in local_temp_files_to_clean:
            if temp_file.exists():
                try:
                    temp_file.unlink()
                except Exception:
                    pass


def main():
    load_env()
    parser = argparse.ArgumentParser(description="Antigravity PDF to Obsidian Vault Parser")
    parser.add_argument("pdf_path", help="PDF 檔案的路徑")
    parser.add_argument("--vault", default=None, help="Obsidian Vault 的絕對路徑（預設會存於當前目錄下的 notes/ 目錄）")
    parser.add_argument("--name", default=None, help="輸出的 Markdown 檔名（不需帶副檔名）")
    parser.add_argument("--prompt", default=None, help="額外的客製化引導提示詞")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini 模型名稱 (預設: {DEFAULT_MODEL})")
    args = parser.parse_args()
    
    result = convert_pdf_to_obsidian(
        pdf_path=args.pdf_path,
        vault_dir=args.vault,
        name=args.name,
        custom_prompt=args.prompt,
        model_name=args.model
    )
    print(result)


if __name__ == "__main__":
    main()
