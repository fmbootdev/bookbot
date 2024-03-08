#!/usr/bin/env python

def main():
    text = read_book("books/frankenstein.txt")
    print(f"Frankenstein contains {count_words(text)} words.")
    letters = count_letters(text)
    print(f"Frankenstein contains the following letter counts:")
    print(letters)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        c = letter.lower()
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

main()
