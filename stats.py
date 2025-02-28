def accept_text():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    amount = len(words)
    return amount

def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

def get_character_num(text):
    characters = {}
    for letters in text:
        characters[letters.lower()] = characters.get(letters.lower(), 0) + 1
    return characters