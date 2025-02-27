def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    result = get_book_text("books/frankenstein.txt")
    print(result)

   

main()