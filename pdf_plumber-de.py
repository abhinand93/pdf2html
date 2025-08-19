import pdfplumber
from html import escape

def pdf_to_html_pdfplumber(pdf_path, output_path):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PDF Content</title>
        <style>
            body { font-family: monospace; margin: 40px; white-space: pre-wrap; }
            .page { margin-bottom: 50px; border: 1px solid #ddd; padding: 20px; }
            table { border-collapse: collapse; width: 100%; margin: 20px 0; }
            td, th { border: 1px solid #ddd; padding: 8px; text-align: left; }
        </style>
    </head>
    <body>
    """
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            html_content += f'<div class="page"><h3>Page {page_num + 1}</h3>'
            
            # Extract text with layout
            text = page.extract_text()
            if text:
                html_content += f'<div>{escape(text)}</div>'
            
            # Extract tables if any
            tables = page.extract_tables()
            for table in tables:
                html_content += '<table>'
                for row in table:
                    html_content += '<tr>'
                    for cell in row:
                        cell_content = escape(str(cell)) if cell else ''
                        html_content += f'<td>{cell_content}</td>'
                    html_content += '</tr>'
                html_content += '</table>'
            
            html_content += '</div>'
    
    html_content += "</body></html>"
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

# Usage
pdf_to_html_pdfplumber(r'C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf', 'output.html')