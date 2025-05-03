import sys, os
from stats import get_num_words, get_char_count, sort_char_count

def list_books_in_directory(directory):
    try:
        files = os.listdir(directory)
        txt_files = []

        for file in files:
            if file.endswith('.txt'):
                txt_files.append(file)
        return txt_files
    except FileNotFoundError:
        return[]

def get_book_text(file_path):
    try:
        with open(file_path) as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)
    except (PermissionError, IOError) as err:
        print(f"Error: Unable to read file '{file_path}': {err}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        
        print("\nAvailable books in 'books/' directory:")
        for book in list_books_in_directory('books'):
            print(f"  - books/{book}")
        
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    char_counts = get_char_count(book_text)
    sorted_chars = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    # print(f"{num_words} words found in the document")
    # print("\nCharacter frequencies:")
    # print(char_counts)

main()