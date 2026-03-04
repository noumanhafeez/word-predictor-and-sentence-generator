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


uni = unigram(tokens)
#print(uni)

bi = bigrams(tokens)
#print(bi)
trig = trigrams(tokens)
#print(trig)

trig_freq = Counter(trig)   # trig is your list of trigrams
bi_freq = Counter(bi)       # bi is your list of bigrams
uni_freq = Counter(uni)