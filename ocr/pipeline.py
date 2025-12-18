from ocr.preprocess import preprocess_image
from ocr.printed import extract_text_printed


def run_printed_ocr(image_path: str) -> str:
    processed_image = preprocess_image(image_path)
    text = extract_text_printed(processed_image)
    return text
