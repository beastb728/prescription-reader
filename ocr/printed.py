import pytesseract
from PIL import Image


def extract_text_printed(image: Image.Image) -> str:
    """
    Extract text from a printed prescription image using Tesseract.
    Expects a preprocessed PIL image.
    Returns raw OCR text.
    """

    text = pytesseract.image_to_string(
        image,
        config="--psm 6"
    )

    return text.strip()
