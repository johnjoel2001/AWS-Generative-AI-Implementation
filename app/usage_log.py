import logging
logging.basicConfig(filename="usage.log", level=logging.INFO)

def log_usage(prompt, style, output):
    logging.info(f"PROMPT ({style}): {prompt[:50]}... | RESULT: {output[:50]}...")
