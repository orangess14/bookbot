def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print(f"{count_words(text)} words found in the document")
    print(f"each character in the document: {count_characters(text)}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = []
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_dict = dict()
    character_dict.update()
    for char in text:
        if char in character_dict:
            character_dict[f'{char}'] += 1
        else:
            character_dict.update({char:1})
        
    return(character_dict)
main()