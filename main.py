from stats import *
import sys

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    list = create_sorted_char_list(count_char(get_book_text(book_path)))
    print_report(list,book_path,word_count)

main()