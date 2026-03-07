import math
from .preprocessing import preprocess
from . import get_prediction


def compute_perplexity(sentence):
    """
    Compute perplexity of a sentence using the trained trigram model.
    """

    # Preprocess the sentence using same pipeline
    tokens = preprocess(sentence)

    # Get trained frequencies from get_prediction
    uni_freq = get_prediction.uni_freq
    bi_freq = get_prediction.bi_freq
    tri_freq = get_prediction.tri_freq
    total_words = get_prediction.total_words

    N = len(tokens)

    if N == 0:
        return float("inf")

    log_prob_sum = 0

    for i in range(1, N):

        # ---------- TRIGRAM ----------
        if i >= 2:
            trigram = (tokens[i-2], tokens[i-1], tokens[i])
            trigram_count = tri_freq.get(trigram, 0)

            bigram_context = (tokens[i-2], tokens[i-1])
            context_count = bi_freq.get(bigram_context, 0)

            if trigram_count > 0 and context_count > 0:
                prob = trigram_count / context_count
                log_prob_sum += math.log(prob)
                continue

        # ---------- BIGRAM ----------
        bigram = (tokens[i-1], tokens[i])
        bigram_count = bi_freq.get(bigram, 0)

        context_count = uni_freq.get(tokens[i-1], 0)

        if bigram_count > 0 and context_count > 0:
            prob = bigram_count / context_count
            log_prob_sum += math.log(prob)
            continue

        # ---------- UNIGRAM ----------
        unigram_count = uni_freq.get(tokens[i], 0)

        if unigram_count > 0:
            prob = unigram_count / total_words
        else:
            prob = 1 / total_words  # avoid log(0)

        log_prob_sum += math.log(prob)

    perplexity = math.exp(-log_prob_sum / N)

    return perplexity