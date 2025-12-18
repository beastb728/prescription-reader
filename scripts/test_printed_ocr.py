from ocr.pipeline import run_printed_ocr

text = run_printed_ocr("data/input/sample.jpg")

print("===== OCR OUTPUT =====")
print(text)
