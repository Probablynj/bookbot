def accept_text():
    text = get_book_text("books/frankenstein.txt")
    return text

def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

def get_character_num(text):
    characters = {}
    for letters in text:
        characters[letters.lower()] = characters.get(letters.lower(), 0) + 1
    return characters

def sort_characters(char_count_dict):
    chars_list = []

    for char, count in char_count_dict.item():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

"""def print_report(filepath, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['count']}")

    print("============== END ==============")"""