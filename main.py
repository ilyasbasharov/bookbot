def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = count_chars(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")

    alphabet = "qwertyuiopasdfghjklzxcvbnm"

    for ch in alphabet:
        print(f"The '{ch}' character was found {chars[ch]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text: str):
    return len(text.split())

def count_chars(text: str):
    res = {}
    for ch in text:
        ch = ch.lower()
        counter = res.setdefault(ch, 0)
        res[ch] = counter + 1
    
    return res

main()