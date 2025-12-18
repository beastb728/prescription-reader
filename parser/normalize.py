import re


def normalize_text(text: str) -> str:
    """
    Clean and normalize raw OCR text from prescriptions.
    """

    if not text:
        return ""

    # unify newlines
    text = text.replace("\r", "\n")

    # remove weird quotes and symbols
    text = re.sub(r"[“”‘’|•■©]", " ", text)

    # remove non-useful characters (keep letters, numbers, basic punctuation)
    text = re.sub(r"[^a-zA-Z0-9\.\,\-\(\)\/\n ]", " ", text)

    # normalize common units
    text = re.sub(r"\bmg\b", "mg", text, flags=re.IGNORECASE)
    text = re.sub(r"\bml\b", "ml", text, flags=re.IGNORECASE)

    # collapse multiple spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # collapse multiple newlines
    text = re.sub(r"\n{2,}", "\n", text)

    # trim lines
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        # drop very short garbage lines
        if len(line) >= 3:
            lines.append(line)

    return "\n".join(lines)
