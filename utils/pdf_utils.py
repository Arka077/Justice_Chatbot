from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import fitz  # PyMuPDF
import os

# ✅ Set the path to your local Poppler installation
POPPLER_PATH = r"C:\Users\ASUS\coding\projects\doj_legal_app\poppler-24.08.0\Library\bin"

def split_exact_half(img: Image.Image):
    """Split an image into left and right halves (for double-page scans)."""
    mid = img.width // 2
    left = img.crop((0, 0, mid, img.height))
    right = img.crop((mid, 0, img.width, img.height))
    return [left, right]

def extract_text_from_pdf_smart(pdf_path, dpi=300, force_double_page=False):
    """
    Extracts text from a PDF file intelligently.
    Uses PyMuPDF for text-based pages, and OCR for scanned images.
    
    Args:
        pdf_path (str): Path to the PDF file
        dpi (int): DPI setting for OCR fallback
        force_double_page (bool): If True, splits OCR images in half
    
    Returns:
        str: Extracted text from the PDF
    """
    final_text = ""
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text().strip()

        # ✅ Use text from PyMuPDF if available
        if len(text) > 100:
            final_text += f"\n[Page {page_num+1} - Text Extracted]\n{text}"
        else:
            # 🔁 OCR fallback for scanned or image-only pages
            print(f"🔁 OCR fallback on page {page_num+1}...")
            images = convert_from_path(
                pdf_path,
                dpi=dpi,
                first_page=page_num + 1,
                last_page=page_num + 1,
                poppler_path=POPPLER_PATH  # ✅ Explicit Poppler path
            )
            img = images[0]

            if force_double_page:
                halves = split_exact_half(img)
                left_text = pytesseract.image_to_string(halves[0])
                right_text = pytesseract.image_to_string(halves[1])
                final_text += f"\n[Page {page_num+1} - Left Half OCR]\n{left_text.strip()}"
                final_text += f"\n[Page {page_num+1} - Right Half OCR]\n{right_text.strip()}"
            else:
                ocr_text = pytesseract.image_to_string(img)
                final_text += f"\n[Page {page_num+1} - OCR Text]\n{ocr_text.strip()}"

    doc.close()
    return final_text.strip()
