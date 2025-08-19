from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
import io

def convert_pdf_to_html(pdf_path, html_path):
    output_html = io.BytesIO()   # ✅ use BytesIO for HTML output
    with open(pdf_path, 'rb') as pdf_file:
        extract_text_to_fp(pdf_file, output_html, laparams=LAParams(), output_type='html')

    html_content = output_html.getvalue().decode("utf-8")  # decode from bytes → string

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"✅ Converted {pdf_path} → {html_path}")

# Example usage
pdf_path = r'C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf'
html_path = 'output.html'
convert_pdf_to_html(pdf_path, html_path)
