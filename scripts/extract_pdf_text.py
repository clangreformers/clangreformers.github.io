import os
import sys
from pikepdf import Pdf, Name, PdfImage, parse_content_stream

def extract_text(pdf_path):
    print("\n--- Content Stream Dump (First 50 ops) ---")
    
    try:
        pdf = Pdf.open(pdf_path)
        page = pdf.pages[0] 
        
        cmds = parse_content_stream(page) 
        
        count = 0
        for operands, operator in cmds:
             print(f"Op: {operator} Args: {repr(operands)}")
             count += 1
             if count > 50:
                 break
        
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    pdf_file = "_posts/2025-12031-2025年总结pptx.pdf"
    cwd = os.getcwd()
    pdf_full_path = os.path.join(cwd, pdf_file)
    extract_text(pdf_full_path)
