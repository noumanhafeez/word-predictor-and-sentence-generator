# get_prediction.py

# Globals (will be set from main.py)
uni_freq = None
bi_freq = None
tri_freq = None
total_words = 0

def set_frequencies(uni, bi, tri):
    """Set the n-gram frequencies for prediction functions."""
    global uni_freq, bi_freq, tri_freq, total_words
    uni_freq = uni
    bi_freq = bi
    tri_freq = tri
    total_words = sum(uni_freq.values())

def predict_next_unigram():
    # P(w) = count(w) / total_words
    max_prob = 0
    next_word = None
    for word, count in uni_freq.items():
        prob = count / total_words
        if prob > max_prob:
            max_prob = prob
            next_word = word
    return next_word

def predict_next_bigram(word):
    # Candidates: all words that follow 'word'
    candidates = [(w2, count) for (w1, w2), count in bi_freq.items() if w1 == word]
    if candidates:
        # MLE probability = count(w1, w2) / count(w1)
        word_count = sum([c for (w2, c) in candidates])  # total bigrams starting with w1
        next_word, _ = max(candidates, key=lambda x: x[1]/word_count)
        return next_word
    return None


def predict_next_trigram(word1, word2):
    # Step 1: Try trigram
    candidates = [(w3, count) for (w1, w2, w3), count in tri_freq.items() if w1 == word1 and w2 == word2]
    if candidates:
        # P(w3 | w1, w2) = count(w1,w2,w3)/count(w1,w2)
        total_count = sum([c for (w3, c) in candidates])
        next_word, _ = max(candidates, key=lambda x: x[1]/total_count)
        return next_word

    # Step 2: Backoff to bigram using word2
    next_word = predict_next_bigram(word2)
    if next_word:
        return next_word

    # Step 3: Backoff to bigram using word1
    next_word = predict_next_bigram(word1)
    if next_word:
        return next_word

    # Step 4: Backoff to unigram
    return predict_next_unigram()
