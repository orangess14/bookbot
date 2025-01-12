def main():
    text = get_book_text("books/frankenstein.txt")
    print("--- Begin report of books/frankenstein.txt ---")
    words = count_words(text)
    print(f"{words} words found in the document")
    chars = dict()
    chars = count_characters(text)
    sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    for char in sorted_chars:
        if char.isalpha() == True:
            print(f"The {char} character was found {sorted_chars[char]} times")

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