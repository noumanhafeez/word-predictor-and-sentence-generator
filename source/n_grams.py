from preprocessing import tokens
from collections import Counter

def unigram(content):
    unigram = content
    return unigram


def bigrams(content):
    bigrams = []

    for i in range(len(content) - 1):
        bigrams.append((content[i], content[i + 1]))
    return bigrams


def trigrams(content):
    trigrams = []
    for i in range(len(content) - 2):
        trigrams.append((content[i], content[i + 1], content[i + 2]))
    return trigrams


# list of single words
unigram = unigram(tokens)
# list of 2-word tuples
bigram = bigrams(tokens)
# list of 3-word tuples
trigram = trigrams(tokens)


trig_freq = Counter(trigram)
bi_freq = Counter(bigram)
uni_freq = Counter(unigram)