import fitz  # pymupdf
import base64
import os

def pdf_to_html_pymupdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PDF Content</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .page { margin-bottom: 50px; border: 1px solid #ddd; padding: 20px; }
            img { max-width: 100%; height: auto; }
        </style>
    </head>
    <body>
    """
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        html_content += f'<div class="page"><h3>Page {page_num + 1}</h3>'
        
        # Get page as HTML (built-in conversion)
        page_html = page.get_text("html")
        html_content += page_html
        
        # Extract images
        image_list = page.get_images()
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Convert to base64 for embedding
            image_base64 = base64.b64encode(image_bytes).decode()
            html_content += f'<img src="data:image/{image_ext};base64,{image_base64}" alt="Image {img_index + 1}">'
        
        html_content += '</div>'
    
    html_content += "</body></html>"
    doc.close()
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

# Usage
pdf_to_html_pymupdf(r'C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf', 'output.html')