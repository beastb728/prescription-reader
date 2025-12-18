from ocr.pipeline import run_printed_ocr
from parser.normalize import normalize_text

raw_text = run_printed_ocr("data/input/sample.jpg")
clean_text = normalize_text(raw_text)

print("===== RAW OCR =====")
print(raw_text)

print("\n===== NORMALIZED TEXT =====")
print(clean_text)
