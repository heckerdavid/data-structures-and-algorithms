def is_anagram(string1, string2):

    string_dict = convert_string_to_dict(string1)

    for letter in string2:
        if string_dict.get(letter):
            string_dict[letter] -= 1
            if string_dict[letter] <= 0:
                del string_dict[letter]
            continue
        return False

    return not bool(string_dict)

def convert_string_to_dict(string):
    str_dict = {}
    for letter in string:
        if str_dict.get(letter):
            str_dict[letter] += 1
        else:
            str_dict[letter] = 1

    return str_dict
