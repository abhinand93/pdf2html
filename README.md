PDF to HTML Conversion Notes

Default Python libraries do not retain layout
Standard libraries like PyPDF2 or pdfminer can extract text, but they do not preserve the original PDF layout.

Use pdf2htmlEX or pdf2html for layout preservation
To maintain the visual layout of a PDF (including formatting, images, and positions), tools like pdf2htmlEX are required.
A Python wrapper or integration such as pdf2html.py depends on these tools being installed.

File naming conventions
Use different filenames to indicate which library or tool is used in each script for clarity (e.g., pdf2text_pypdf2.py, pdf2html_pdf2htmlEX.py, etc.).
