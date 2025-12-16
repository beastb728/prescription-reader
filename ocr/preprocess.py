import cv2
import numpy as np
from PIL import Image


def preprocess_image(image_path: str) -> Image.Image:
    """
    Load image and apply preprocessing to improve OCR accuracy.
    Returns a PIL Image.
    """

    # read image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Unable to read image: {image_path}")

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # denoise
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)

    # adaptive thresholding
    processed = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # convert to PIL Image
    pil_image = Image.fromarray(processed)

    return pil_image
