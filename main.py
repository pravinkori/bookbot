from stats import get_chars_dict, get_num_words


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    chars_dict = get_chars_dict(text)
    print(chars_dict)


main()
