def count_words(book_string):
    word_count = book_string.split()
    return f"Found {len(word_count)} total words"

def count_char(book_string):
    char_dict = {}
    for char in book_string.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char]+=1
    return char_dict
    
def sort_on(char_dict):
    return char_dict["num"]

def create_sorted_char_list(char_dict):
    list = []
    for char,value in char_dict.items():
        if char.isalpha():
            list.append({"char": char,"num":value})
    list.sort(reverse=True,key=sort_on)
    return list

def print_report(list,path,word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"{word_count}")
    print("--------- Character Count -------")
    for dict in list:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
