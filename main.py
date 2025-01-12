def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print(count_words(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_words(text):
    words = []
    words = text.split()
    return len(words)
main()