import re
import string

from data_ingestion import content

def clean_text(text):

    # lower text
    text = text.lower()

    # remove links
    text = re.sub('www\.\S+', '', text)

    # remove BOM
    text = text.replace('\ufeff', '')

    # remove brackets, underscore, slash
    text = re.sub(r'[\[\]_]', '', text)

    # remove all those like dots instead of words, numbers etc.
    text = re.sub(r'[^\w\s\']', '', text)

    # remove extra spacing
    text = " ".join(text.split())

    # remove Project Gutenberg header
    text = re.sub(r'project gutenberg.*?start of the project gutenberg ebook', '', text, flags=re.I | re.S)
    # remove end of the project Gutenberg footer
    text = re.sub(r'illustration end of the project gutenberg ebook.*', '', text, flags=re.I | re.S)

    return text


clean_data = clean_text(content)
print(clean_data)
