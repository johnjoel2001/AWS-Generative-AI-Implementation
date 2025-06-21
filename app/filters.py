BAD_WORDS = ["badword1", "nastyword", "kill", "hate", "bomb"]

def is_safe(text):
    text_lower = text.lower()
    return not any(bad in text_lower for bad in BAD_WORDS)
