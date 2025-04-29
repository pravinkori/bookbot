def get_book_test(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_test(book_path)

    print(book_text)

main()