# n_grams.py
from collections import Counter

def get_unigram(tokens):
    """
    Return list of unigrams (single tokens).
    """
    return tokens


def get_bigrams(tokens):
    """
    Return list of bigrams(2 words) as tuples.
    """

    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))
    return bigrams


def get_trigrams(tokens):
    """
    Return list of trigrams (3 words) as tuples.
    """

    trigrams = []
    for i in range(len(tokens) - 2):
        trigrams.append((tokens[i], tokens[i + 1], tokens[i + 2]))
    return trigrams


def get_ngram_frequencies(tokens):
    """
    Return frequency counters for uni, bi, and trigrams.
    """

    unigrams = get_unigram(tokens)
    bigrams = get_bigrams(tokens)
    trigrams = get_trigrams(tokens)

    uni_freq = Counter(unigrams)
    bi_freq = Counter(bigrams)
    tri_freq = Counter(trigrams)

    return uni_freq, bi_freq, tri_freq