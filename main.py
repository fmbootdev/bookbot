#!/usr/bin/env python

def main():
    text = read_book("books/frankenstein.txt")
    word_count = count_words(text)
    letter_counts = count_letters(text)
    print(word_count)
    print(letter_counts)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        ci_char = char.lower()
        if ci_char.isalpha():
            if ci_char in letters:
                letters[ci_char] += 1
            else:
                letters[ci_char] = 1
    return letters

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

main()
