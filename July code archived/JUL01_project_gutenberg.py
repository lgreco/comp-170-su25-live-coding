# JUL 01
import requests

book_url = "https://www.gutenberg.org/cache/epub/98/pg98.txt"

# Establish connection to website

connection = requests.get(book_url, stream=True)

line_counter = 0
word_count = 0
for line in connection.iter_lines():
    if line:
        line_counter += 1
        word_count += len(line.split())

print(f"There are {line_counter:,d} lines in the book")
print(f"THere are {word_count:,d} words.")



some_words = ["it", "was", "a", "dark", "and", "stormy", "night"]
char_count = 0
for word in some_words:
    char_count += len(word)
print(char_count)