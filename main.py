def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words in {book_path}")
    print(get_num_letters(text))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letters = {}
    lowercase_string = text.lower()
    for letter in lowercase_string:
        if letter != " ":
            if letter in letters:
                letters[letter] = letter
            else:
                letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["num"]


main()

