from stats import word_count, sorted_counts, character_count, sort_by_num
import sys

def get_book_text(book_file_path):
    with open(book_file_path) as content:
        return content.read()

def main():
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]} ...
----------- Word Count ----------""")
    total_word_count = word_count(get_book_text(sys.argv[1]))
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")
    individual_word_count_dict = sorted_counts(get_book_text(sys.argv[1]))
    for dictionnary in individual_word_count_dict:
        print(f"{dictionnary['char']}: {dictionnary['num']}")
    print("============= END ===============")

if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()


