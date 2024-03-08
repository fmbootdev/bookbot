#!/usr/bin/env python

def main():
    text = read_book("books/frankenstein.txt")
    word_count = count_words(text)
    character_counts = count_characters(text)
    print(word_count)
    print(character_counts)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        ci_char = char.lower()
        if ci_char in characters:
            characters[ci_char] += 1
        else:
            characters[ci_char] = 1
    return characters

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

main()
