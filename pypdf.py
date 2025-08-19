import PyPDF2
from html import escape

def pdf_to_html_pypdf2(pdf_path, output_path):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PDF Content</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .page { margin-bottom: 50px; border-bottom: 1px solid #ccc; padding-bottom: 20px; }
        </style>
    </head>
    <body>
    """
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            html_content += f'<div class="page"><h3>Page {page_num + 1}</h3>'
            html_content += f'<p>{escape(text).replace(chr(10), "<br>")}</p></div>'
    
    html_content += "</body></html>"
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

# Usage
pdf_to_html_pypdf2(r'C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf', 'output.html')