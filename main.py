from stats import get_num_words, get_char_count

def get_book_test(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_test(book_path)

    num_words = get_num_words(book_text)
    char_counts = get_char_count(book_text)

    print(f"{num_words} words found in the document")
    print("\nCharacter frequencies:")
    print(char_counts)

main()