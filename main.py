def main():
    book_path = "books/frankenstein.txt"
    text = read_the_text(book_path)
    word_count = count(text)
    letter_amounts = letter_count(text)
    dict_list = dict_lister(letter_amounts)
    count(text)
    letter_count(text)
    dict_lister(letter_amounts)
    dictionary_sort(dict_list)
    report(book_path, word_count, dict_list)

def read_the_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

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
            letter_amounts[letter] += 1
            
    return letter_amounts


def dict_lister(letter_amounts):
    dict_list = [{"letter": l, "value": v} for l, v in letter_amounts.items()]
    return dict_list

def sort_on(dict_list):
    return dict_list["value"]

def dictionary_sort(dict_list):
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

    
def report(book_path, word_count, dict_list):
        print(f"--- Begin report of {book_path} --- \r\n")
        print(f"{word_count} words found in the document \r\n")
        for f in dict_list:
            print(f"the {f["letter"]} character was found {f["value"]} times")
        print("--- End report---")


if __name__ == "__main__":
    main() 
