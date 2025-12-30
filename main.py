from stats import word_counter, char_counter, dict_sorter
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_counter(text)
    frequencies = char_counter(text) 
    sorted_dict = dict_sorter(frequencies)
    print_report(book_path, num_words, sorted_dict)

def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
