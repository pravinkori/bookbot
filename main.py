from stats import (
    chars_dict_to_sorted_list,
    get_chars_dict,
    get_num_words,
)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    chars_dict = get_chars_dict(text)
    print(chars_dict)

    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


main()
