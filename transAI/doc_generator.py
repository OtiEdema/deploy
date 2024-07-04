import pdfkit
from docx import Document

def save_as_pdf(text, filename="transcription.pdf"):
    html_content = "<html><body><p>{}</p></body></html>".format(text.replace('\n', '<br>'))

    pdfkit.from_string(html_content, filename)

def save_as_word(text, filename="transcription.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
