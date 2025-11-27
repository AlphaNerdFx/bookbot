def word_count(book):
    word_list = book.split()
    word_count = len(word_list)
    return word_count

def character_count(book):
    word_list = book.split()
    word_list = [word.lower() for word in word_list]
    character_dict = {}
    for word in word_list:
        for i in word:
            if(character_dict.get(i)):
                character_dict[i] += 1
            else:    
                character_dict[i] = 1
    alphabetic_character_dict = {}
    for character in character_dict:
        if character.isalpha():
            alphabetic_character_dict[character] = character_dict[character]
    return alphabetic_character_dict

def sort_by_num(dict):
    return dict["num"]

def sorted_counts(book):
    character_counts = character_count(book)
    detailed_character_counts = []
    for character in character_counts:
        detailed_character_counts.append({"char" : character, "num" : character_counts[character]})
    detailed_character_counts.sort(reverse=True, key = sort_by_num)
    return detailed_character_counts