def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

def main():
    get_book_text("books/frankenstein.txt")
    return get_book_text()
print(get_book_text)
   

main()