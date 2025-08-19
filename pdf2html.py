import subprocess
import os

def pdf_to_html_poppler(pdf_path, output_dir):
    # Create absolute path and ensure directory exists
    abs_output_dir = os.path.abspath(output_dir)
    os.makedirs(abs_output_dir, exist_ok=True)
    
    # Run the conversion
    output_path = os.path.join(abs_output_dir, 'output.html')
    subprocess.run(['pdftohtml', '-c', '-noframes', pdf_path, output_path])

# Usage
pdf_to_html_poppler(r'C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf', 'output')