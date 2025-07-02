# JUL 02

import requests

book_url = "https://www.gutenberg.org/cache/epub/98/pg98.txt"

# Establish connection to PG webserver
connection = requests.get(book_url)
# Initialize a dictionary to count word frequencies
frequency_of = dict()

for text_line in connection.iter_lines():
    # make sure line is not empty
    if text_line:
        text_line = text_line.decode('utf-8')
        words = text_line.split()
        for word in words:
            # Ask if this word is in the dictionary
            if word in frequency_of:
                frequency_of[word] = frequency_of[word] + 1
            else:
                frequency_of[word] = 1

print(f"\n\nThere are {len(frequency_of):,d} words in the book\n")

highest_frequency = 0
most_frequent_word = ""
# iterate over the dictionary, obtaining its key-value pairs, one at a time
for word, count in frequency_of.items():
    if count > highest_frequency:
        highest_frequency = count
        most_frequent_word = word
    if count == 1:
        print(f"\nunique word: {word}")

print(f"\n{most_frequent_word=} with {highest_frequency=}\n")




