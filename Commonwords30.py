import re
import operator
import csv
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def preprocess_text(text):
    text = re.sub('[^a-zA-Z0-9\s]', '', text).lower()
    words = text.split()
    return words

def count_word_occurrences(words):
    word_counts = Counter(words)
    return word_counts

def get_top_30_words(word_counts):
    sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    top_30_words = sorted_word_counts[:30]
    return top_30_words

def save_to_csv(top_30_words, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, count in top_30_words:
            writer.writerow({'word': word, 'count': count})

def count_word_occurrences_in_text_file(file_path, csv_file_path):
    text = read_file(file_path)
    words = preprocess_text(text)
    word_counts = count_word_occurrences(words)
    top_30_words = get_top_30_words(word_counts)
    save_to_csv(top_30_words, csv_file_path)

if __name__ == "__main__":
    input_file = "output.txt"
    output_csv = "top_30_words.csv"
    count_word_occurrences_in_text_file(input_file, output_csv)