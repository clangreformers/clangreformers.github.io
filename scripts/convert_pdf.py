import os
import sys
import subprocess
from pikepdf import Pdf

def convert_pdf_to_images(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Opening PDF: {pdf_path}")
    try:
        pdf = Pdf.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        sys.exit(1)

    print(f"Total pages: {len(pdf.pages)}")
    
    generated_images = []

    for i, page in enumerate(pdf.pages):
        page_num = i + 1
        # Create a temporary single-page PDF
        temp_pdf_path = os.path.join(output_dir, f"temp_page_{page_num:02d}.pdf")
        dst = Pdf.new()
        dst.pages.append(page)
        dst.save(temp_pdf_path)

        # Output image path
        image_name = f"slide_{page_num:02d}.png"
        image_path = os.path.join(output_dir, image_name)

        # Convert using sips (macOS built-in)
        # -s format png : set format to png
        # --out : output file
        cmd = ["sips", "-s", "format", "png", temp_pdf_path, "--out", image_path]
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            print(f"Generated: {image_name}")
            generated_images.append(image_name)
        except subprocess.CalledProcessError as e:
            print(f"Error converting page {page_num}: {e}")
        finally:
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)
    
    return generated_images

if __name__ == "__main__":
    pdf_file = "_posts/2025-12031-2025年总结pptx.pdf"
    out_dir = "assets/imgs/2025_summary/"
    
    # Adjust paths to be absolute or relative to CWD
    cwd = os.getcwd()
    pdf_full_path = os.path.join(cwd, pdf_file)
    out_full_dir = os.path.join(cwd, out_dir)

    if not os.path.exists(pdf_full_path):
        print(f"PDF file not found at: {pdf_full_path}")
        # Try finding it without relative path if script run from wrong dir
        if os.path.exists(pdf_file):
             pdf_full_path = pdf_file
        else:
             sys.exit(1)

    convert_pdf_to_images(pdf_full_path, out_full_dir)
