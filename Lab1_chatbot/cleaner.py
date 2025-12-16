# cleaner.py
import re

def clean_corpus(chat_file):
    # Matches WhatsApp date, time (am/pm), name, and colon
    pattern = r"^\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s?(?:am|pm|AM|PM)\s-\s.*?:\s"

    messages = []

    with open(chat_file, "r", encoding="utf-8") as f:
        for line in f:
            line = re.sub(pattern, "", line).strip()
            if line and "<Media omitted>" not in line:
                messages.append(line)

    return messages
