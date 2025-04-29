def get_book_test(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_test(book_path)

    num_words = count_words(book_text)

    print(f"{num_words} words found in the document")

main()