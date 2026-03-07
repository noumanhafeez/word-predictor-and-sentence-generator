from .get_prediction import predict_next_unigram, predict_next_bigram, predict_next_trigram


MAX_LEN = 30

def generate_sentence(start_words=None):
    """
        Generate a sentence using trigram language model with backoff.

        Parameters:
            start_words (list of str, optional): 0, 1, or 2 starting words.

        Returns:
            str: Generated sentence without <s> and </s> tokens.
        """

    # Initialize sentence
    if not start_words:
        sentence = ['<s>']

    elif len(start_words) == 1:
        sentence = ['<s>', start_words[0]]

    else:
        sentence = ['<s>', start_words[0], start_words[1]]

    # Generate words
    while len(sentence) < MAX_LEN:

        # If we have at least 2 words → trigram
        if len(sentence) >= 3:
            next_word = predict_next_trigram(sentence[-2], sentence[-1])

        # If only one word after <s> → bigram
        elif len(sentence) == 2:
            next_word = predict_next_bigram(sentence[1])

        # Only <s> → unigram
        else:
            next_word = predict_next_unigram()


        if not next_word or next_word == '</s>':
            break

        sentence.append(next_word)


    return " ".join([w for w in sentence[1:] if w != '</s>'])