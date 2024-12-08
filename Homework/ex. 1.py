from collections import Counter
import string

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        word_count = Counter(words)
        print("Word Frequencies:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")

file_path = "example.txt"
count_word_frequency(file_path)
