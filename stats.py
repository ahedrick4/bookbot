def word_count(words):
    new_array = words.split()
    return len(new_array)

def letter_count(text):
    new_array = text.split()
    new_dict = {}
    for word in new_array:
        for letter in word:
            new_letter = letter.lower()
            if new_letter not in new_dict:
                new_dict[new_letter] = 1
            else:
                new_dict[new_letter] += 1
    return new_dict

def helper_func(e):
    return e['num']

def generate_sorted_report(unsorted):
    sorted_list = []
    for item in unsorted:
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = unsorted[item]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=helper_func)
    return sorted_list