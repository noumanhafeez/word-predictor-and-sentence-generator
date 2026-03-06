# main.py

from pipeline import run_pipeline
from get_prediction import predict_next_unigram, predict_next_bigram, predict_next_trigram
from sentence_generator import generate_sentence


def user_interaction():
    """
    Interactive user input for next-word prediction or sentence generation.
    """
    print("\n--- N-gram Next Word Prediction & Sentence Generation ---")
    while True:
        choice = input("\nChoose an option:\n1. Predict next word\n2. Generate sentence\n3. Exit\n> ")
        if choice == '1':
            words = input("Enter 1 or 2 words (space-separated): ").strip().lower().split()
            if len(words) == 1:
                print("Predicted next word:", predict_next_bigram(words[0]))
            elif len(words) == 2:
                print("Predicted next word:", predict_next_trigram(words[0], words[1]))
            else:
                print("Please enter only 1 or 2 words.")
        elif choice == '2':
            words = input("Enter 0, 1, or 2 starting words (space-separated, blank for none): ").strip().lower().split()
            print("Generated sentence:", generate_sentence(words if words else None))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    # Replace with your Gutenberg file path
    file_path = '../gutenberg.txt'

    # Run the pipeline
    run_pipeline(file_path)

    # Start user interaction
    user_interaction()