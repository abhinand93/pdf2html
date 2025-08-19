# No design or styles

import fitz # PyMuPDF

def pdf_to_html(input_pdf, output_html):
    doc = fitz.open(input_pdf)
    html_content = ""

    for page in doc:
        html_content += page.get_text("html")  # extract page as HTML

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Converted {input_pdf} → {output_html}")

# Example usage
pdf_to_html(r"C:\Users\abhin\Documents\rt-agentic-ai-cert-week2\demo\filewithissue.pdf", "output.html")
