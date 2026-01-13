import os
import sys
from pikepdf import Pdf, Name, PdfImage

def extract_content(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf = Pdf.open(pdf_path)
    page = pdf.pages[0] # Assume 1 page

    # 1. Extract Images
    print("--- Images ---")
    image_count = 0
    for name, image in page.images.items():
        pdf_image = PdfImage(image)
        out_name = f"extracted_image_{image_count}.png"
        out_path = os.path.join(output_dir, out_name)
        pdf_image.extract_to(fileprefix=out_path)
        print(f"Extracted image: {out_name} (Size: {pdf_image.width}x{pdf_image.height})")
        image_count += 1

    # 2. Extract Text (Rudimentary)
    print("\n--- Text Content (Raw) ---")
    content_stream = page.get_contents()
    if content_stream:
        # Read commands
        from pikepdf.models.content_stream import parse_content_stream
        
        # We need to manually parse because pikepdf doesn't have a high-level text extractor
        # This is a heuristic attempts to find text strings in the stream
        commands = parse_content_stream(content_stream)
        text_content = []
        for operands, operator in commands:
             if operator == b'Tj':
                 text_content.append(str(operands[0]))
             elif operator == b'TJ':
                 for item in operands[0]:
                     if isinstance(item, (str, bytes)):
                         text_content.append(str(item))
        
        print("\n".join(text_content))

if __name__ == "__main__":
    pdf_file = "_posts/2025-12031-2025年总结pptx.pdf"
    out_dir = "assets/imgs/2025_summary_extracted/"
    
    cwd = os.getcwd()
    pdf_full_path = os.path.join(cwd, pdf_file)
    out_full_dir = os.path.join(cwd, out_dir)
    
    extract_content(pdf_full_path, out_full_dir)
