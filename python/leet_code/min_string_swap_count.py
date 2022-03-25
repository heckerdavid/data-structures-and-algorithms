# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

def count_swaps(string1, string2):
    count = 0

    string_one_characters = {}
    for char in string1:
        if string_one_characters.get(char):
            string_one_characters[char] += 1
        else:
            string_one_characters[char] = 1

    for char in string2:
        if string_one_characters.get(char) and string_one_characters.get(char) > 1:
            string_one_characters[char] -= 1
        elif string_one_characters.get(char):
            del string_one_characters[char]
        else:
            count += 1

    return count
