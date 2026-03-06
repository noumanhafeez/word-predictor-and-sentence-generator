# main.py

from data_ingestion import openfile
from preprocessing import preprocess
from n_grams import unigram, bigrams, trigrams, Counter
from get_prediction import predict_next_unigram, predict_next_bigram, predict_next_trigram
from sentence_generator import generate_sentence


def run_pipeline(file_path: str):
    """
    Run the full NLP pipeline: load data, preprocess, build n-grams, and show examples.
    """
    print("Loading data...")
    data = openfile(file_path)
    if not data:
        print("No content loaded. Exiting.")
        return

    print("Preprocessing text...")
    tokens = preprocess(data)
    print(f"Total tokens: {len(tokens)}")

    print("Building N-grams...")
    unigrams = unigram(tokens)
    bigram = bigrams(tokens)
    trigram = trigrams(tokens)

    # Build frequency counters
    uni_freq = Counter(unigrams)
    bi_freq = Counter(bigram)
    tri_freq = Counter(trigram)

    print("\nExample Predictions:")
    print("-------------------")
    print(f"Most likely unigram: {predict_next_unigram()}")
    print(f"Next word after 'alice': {predict_next_bigram('alice')}")
    print(f"Next word after 'in the': {predict_next_trigram('in', 'the')}")

    print("\nExample Sentences:")
    print("-----------------")
    print("Random sentence:", generate_sentence())
    print("Sentence starting with 'tarts':", generate_sentence(['tarts']))
    print("Sentence starting with 'in the':", generate_sentence(['in', 'the']))


def user_interaction():
    """
    Take user input for prediction or sentence generation.
    """
    print("\n--- N-gram Next Word Prediction & Sentence Generation ---")
    while True:
        choice = input("\nChoose an option:\n1. Predict next word\n2. Generate sentence\n3. Exit\n> ")

        if choice == '1':
            words = input("Enter one or two words (space-separated): ").strip().lower().split()
            if len(words) == 1:
                next_word = predict_next_bigram(words[0])
                print(f"Predicted next word: {next_word}")
            elif len(words) == 2:
                next_word = predict_next_trigram(words[0], words[1])
                print(f"Predicted next word: {next_word}")
            else:
                print("Please enter only 1 or 2 words.")

        elif choice == '2':
            words = input(
                "Enter 0, 1, or 2 starting words (space-separated, leave blank for none): ").strip().lower().split()
            sentence = generate_sentence(words if words else None)
            print(f"Generated sentence: {sentence}")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    # Replace with your Gutenberg file path
    file_path = '../gutenberg.txt'
    run_pipeline(file_path)
    user_interaction()