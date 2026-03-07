# pipeline.py

from .data_ingestion import read_file
from .preprocessing import preprocess
from .n_grams import get_ngram_frequencies
from .get_prediction import set_frequencies, predict_next_unigram, predict_next_bigram, predict_next_trigram
from .sentence_generator import generate_sentence

def run_pipeline(file_path):
    """
    Run the full NLP pipeline:
    - Load data
    - Preprocess
    - Build n-grams
    - Set frequencies for prediction
    - Show example predictions and sentences
    """
    print("Loading data...")
    data = read_file(file_path)
    if not data:
        print("No content loaded. Exiting.")
        return

    print("Preprocessing text...")
    tokens = preprocess(data)
    print(f"Total tokens: {len(tokens)}")

    print("Building N-grams...")
    uni_freq, bi_freq, tri_freq = get_ngram_frequencies(tokens)
    set_frequencies(uni_freq, bi_freq, tri_freq)

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
    Interactive user input for next-word prediction or sentence generation.
    """
    print("\n--- N-gram Next Word Prediction & Sentence Generation ---")
    while True:
        choice = input("\nChoose an option:\n1. Predict next word\n2. Generate sentence\n3. Exit\n> ")

        if choice == '1':
            words = input("Enter 0, 1, or 2 words (space-separated, leave blank for unigram): ").strip().lower().split()

            if len(words) == 0:
                print("Predicted next word (unigram):", predict_next_unigram())
            elif len(words) == 1:
                print("Predicted next word (bigram):", predict_next_bigram(words[0]))
            elif len(words) == 2:
                print("Predicted next word (trigram):", predict_next_trigram(words[0], words[1]))
            else:
                print("Please enter only up to 2 words.")

        elif choice == '2':
            words = input("Enter 0, 1, or 2 starting words (space-separated, blank for none): ").strip().lower().split()
            print("Generated sentence:", generate_sentence(words if words else None))

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")