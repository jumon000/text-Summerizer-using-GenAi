import PyPDF2
import docx
import re

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Ensure non-empty text
                text += page_text + "\n"
    return text

def extract_text_from_docx(docx_path):
    """Extracts text from a DOCX file."""
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])  # Only add non-empty paragraphs

def save_extracted_text(file_path, output_file="extracted_text.txt"):
    """Extracts text from PDF or DOCX and saves it."""
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format! Please provide a PDF or DOCX.")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

def preprocess_text(text):
    """
    Preprocesses the extracted text by:
    - Removing extra whitespace and newlines
    - Removing special characters (optional)
    - Normalizing text (e.g., lowercasing, if needed)
    """
    # Remove extra whitespace and newlines
    text = re.sub(r"\s+", " ", text).strip()
    
    # Remove special characters (optional, depending on the use case)
    text = re.sub(r"[^\w\s.,;:!?()-]", "", text)
    
    # Normalize text (e.g., convert to lowercase if needed)
    text = text.lower()  # Optional, depending on the use case
    
    return text
