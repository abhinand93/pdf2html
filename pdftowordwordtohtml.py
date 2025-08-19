from pdf2docx import Converter
import mammoth

def pdf_to_html(pdf_path, html_path):
    docx_path = "temp.docx"

    # Step 1: Convert PDF → DOCX
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)  # full doc
    cv.close()

    # Step 2: Convert DOCX → HTML (clean, semantic)
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html_content = result.value  # Extracted HTML
        messages = result.messages   # Any conversion warnings

    # Step 3: Save HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Converted {pdf_path} → {html_path}")
    if messages:
        print("⚠️ Warnings:", messages)


# Example usage
pdf_path = r"C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf"
html_path = "output.html"
pdf_to_html(pdf_path, html_path)
