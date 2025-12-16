from ocr.preprocess import preprocess_image

img = preprocess_image("data/input/sample.jpg")
img.save("data/output/preprocessed_sample.png")

print("Saved preprocessed image to data/output/preprocessed_sample.png")
