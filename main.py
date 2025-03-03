from stats import accept_text
from stats import get_character_num
from stats import sort_characters

def print_report(filepath, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['count']}")

    print("============== END ==============")

def main():
    result = accept_text()
    word_count = len(result.split())
    report = sort_characters()
    letters_result = get_character_num(result)
    printReport = print_report(result, word_count, char_count_dict)
    
    print(f"{word_count} words found in the document")
    print(letters_result)
    print(printReport)
    

    

main()