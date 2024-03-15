def main():
    book_path = "books/frankenstein.txt"
    text = read_the_text(book_path)
#    print(type(text))
    count(text)
#    print(text)

def read_the_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    print(word_count)


if __name__ == "__main__":
    main()
