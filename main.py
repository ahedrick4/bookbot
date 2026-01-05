from stats import word_count, letter_count, generate_sorted_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    character_counter = generate_sorted_report(letter_count(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")
    for item in character_counter:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()