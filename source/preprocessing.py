import re

def preprocess(text):


    # 1. Remove Project Gutenberg header
    text = re.sub(r"The Project Gutenberg.*SAM'L GABRIEL SONS & COMPANY\s+NEW YORK", '', text, flags=re.I | re.S)

    # 2. Remove Project Gutenberg footer (everything after [Illustration] or END marker)
    text = re.sub(r"\*\*\* end of the project.*", '', text, flags=re.I | re.S)

    # 3. Lowercase
    text = text.lower()

    # 4. Replace newlines and tabs with space
    text = re.sub(r'\s+', ' ', text)

    # 5. Split into sentences using ., ?, !
    sentences = re.split(r'[.!?]+', text)


    # 6. Add boundary tokens
    tokens = []

    for sentence in sentences:

        # Split sentence into words
        sentence_tokens = sentence.split()

        # Clean words and remove empty strings
        clean_tokens = []
        for word in sentence_tokens:
            word_clean = re.sub(r"[^\w']+", '', word)  # keep letters, digits, apostrophes
            if word_clean:
                clean_tokens.append(word_clean)

        # Add boundary tokens if sentence is not empty
        if clean_tokens:
            tokens += ['<s>'] + clean_tokens + ['</s>']
    return tokens
