from stats import accept_text
from stats import get_character_num

def main():
    result = accept_text()
    letters_result = get_character_num(result)
    print(f"{result} words found in the document")
    print(letters_result)
    

main()