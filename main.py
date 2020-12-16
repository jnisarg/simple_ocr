import argparse
from ocr_oop import OCR

# This is a simple command line based program which takes image or pdf file as an argument and returns
# the extracted text from it. It also has a "--save" argument if you need to save it to the output file.


parser = argparse.ArgumentParser(prog="OCR", description="OCR", allow_abbrev=False)

parser.add_argument("file", type=str, help="image or pdf file for OCR.")
parser.add_argument("-c", "--config", type=str, default=r"--oem 3 --psm 6", help="config to load in tesseract")
parser.add_argument("--text", action="store_true", help="converts file to text")
parser.add_argument("--save", action="store_true", help="saves output in a txt or docx format")
args = parser.parse_args()

ocr = OCR(args.file, args.config)

IMG_EXT = ["bmp", "pnm", "png", "jfif", "jpeg", "jpg", "tiff", "webp", "ppm"]

if args.text:
    if ocr.input_type == "pdf":
        ocr.pdf_to_text(save=args.save)
    elif ocr.input_type in IMG_EXT:
        ocr.img_to_text(save=args.save)
