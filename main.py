#!/usr/bin/env python

def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    word_count = count_words(text)
    letter_counts = count_letters(text)
    print(get_report(path, word_count, letter_counts))

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

def get_report(book_path, word_count, letter_counts):
    report = get_report_preamble(book_path, word_count)
    lc_list = collect_letter_counts(letter_counts)
    lc_list = sort_letter_counts(lc_list)
    report = add_letter_counts(lc_list, report)
    return report

def get_report_preamble(book_path, word_count):
    return (
        f"--- Begin report of {book_path} ---\n"
        f"{word_count} words found in the document\n"
        f"\n"
    )

def collect_letter_counts(letter_counts):
    lc_list = []
    for key in letter_counts.keys():
        lc_list.append({"letter": key, "count": letter_counts[key]})
    return lc_list

def sort_letter_counts(lc_list):
    def sort_on(dict):
        return dict["count"]
    lc_list.sort(reverse=True, key=sort_on)
    return lc_list

def add_letter_counts_to_report(lc_list, report):
    for l in lc_list:
        report += f"The '{l["letter"]}' character was found {l["count"]} times\n"
    return report

def add_letter_counts(lc_list, report):
    report = add_letter_counts_to_report(lc_list, report)
    return report

main()
