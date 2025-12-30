def word_counter(text):
    return len(text.split())

def char_counter(text):
    text = text.lower()
    new_dict = {}
    for char in text:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict

def sort_on(d):
    return d["num"]

def dict_sorter(new_dict): 
    new_list = []
    for ch in new_dict:
        new_list.append({"char": ch, "num": new_dict[ch]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list