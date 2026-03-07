# main.py

from source.user_pipeline import run_pipeline
from source.user_pipeline import user_interaction

if __name__ == "__main__":
    file_path = 'gutenberg.txt'

    # Run the full pipeline
    run_pipeline(file_path)

    # Start user interaction
    user_interaction()



# Bonus Part

from source.perplexity import compute_perplexity

sentence = "one side to look through into the garden with one eye"
random_sentence = "I love programming in Python"

perplexity = compute_perplexity(sentence)
print("\nBonus Part: Perplexity Results")
print("-------------------")
print("Book sentence:", compute_perplexity(sentence))
print("Random sentence:", compute_perplexity(random_sentence))