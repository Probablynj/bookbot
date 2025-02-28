def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

def accept_text():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    amount = len(words)
    return amount
    

def main():
    result = accept_text()
    print(f"{result} words found in the document")

   

main()