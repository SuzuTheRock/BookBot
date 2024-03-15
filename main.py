def main():
    book_path = "books/frankenstein.txt"
    text = read_the_text(book_path)
    count(text)
    letter_count(text)

def read_the_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    print(word_count)

def letter_count(text):
    letter_amounts = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0, 
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in letter_amounts:
            letter_amounts += 1
    print(letter_amounts)

if __name__ == "__main__":
    main()
