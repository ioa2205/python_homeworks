import os
import string
from collections import Counter

def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    return text.translate(str.maketrans("", "", string.punctuation)).lower()

def get_word_frequencies(filename):
    """Reads the file and counts word frequencies."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Please enter a paragraph to create the file.")
        with open(filename, "w") as f:
            text = input("Enter text: ")
            f.write(text)
    
    with open(filename, "r") as f:
        text = f.read()
    
    words = clean_text(text).split()
    word_count = Counter(words)
    
    return words, word_count

def save_report(word_count, total_words, top_n=5, output_file="word_count_report.txt"):
    """Saves the word frequency report to a file."""
    with open(output_file, "w") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write("Top Words:\n")
        for word, count in word_count.most_common(top_n):
            f.write(f"{word} - {count}\n")

def main():
    filename = "sample.txt"
    words, word_count = get_word_frequencies(filename)
    total_words = len(words)

    # Ask user for the number of top words to display
    try:
        top_n = int(input("How many top words to display? (default 5): ") or 5)
    except ValueError:
        top_n = 5  # Default to 5 if input is invalid

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in word_count.most_common(top_n):
        print(f"{word} - {count} times")

    save_report(word_count, total_words, top_n)

if __name__ == "__main__":
    main()
