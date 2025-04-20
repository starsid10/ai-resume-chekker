# resume_parser.py
from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(file):
    text = ""
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
