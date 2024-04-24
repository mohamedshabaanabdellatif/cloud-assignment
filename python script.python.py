import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# Read the contents of the file
def read_file(file_path):
    try:
        with open("C:\Users\2022\Desktop\cloud assignment\paragraphs.txt", 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Remove stop words and punctuation
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    words = nltk.word_tokenize(text.lower())
    filtered_words = [word.translate(translator) for word in words if word not in stop_words]
    return filtered_words

# Count word frequencies
def count_word_frequencies(words):
    word_counts = Counter(words)
    return word_counts

# Display word frequency count
def display_word_frequencies(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Main function
def main():
    file_path = "random_paragraphs.txt"
    text = read_file(file_path)
    if text:
        words = preprocess_text(text)
        word_counts = count_word_frequencies(words)
        display_word_frequencies(word_counts)

if __name__ == "__main__":
    main()