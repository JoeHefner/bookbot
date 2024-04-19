def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_count = get_num_letters(text)
    letters_sort = sort_letters(letters_count)
    for letter in letters_sort:
        print(f"The '{letter['char']}' was found{letter['num']} times.")

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
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sort_letters(dict):
    letter_list = []
    for entry in dict:
        new_dict = {'char' : entry, "num" : dict[entry]}
        letter_list.append(new_dict) 
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def sort_on(dict):
    return dict["num"]


main()

