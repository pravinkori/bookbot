def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents


def get_word_count(text):
    words = text.split()
    return len(words)


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_word_count(text)
    print(f"Found {num_words} total words")


main()
