# pipeline.py

from data_ingestion import read_file
from preprocessing import preprocess
from n_grams import get_ngram_frequencies
from get_prediction import set_frequencies, predict_next_unigram, predict_next_bigram, predict_next_trigram
from sentence_generator import generate_sentence

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