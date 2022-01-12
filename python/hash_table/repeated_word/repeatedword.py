def repeated_word(string):
    word_list = convert_str_to_list(string)
    first_repeat = find_repeated(word_list)
    return first_repeat

def convert_str_to_list(string):

    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''

    for char in string:
        if char in punctuation:
            string = string.replace(char, '')

    as_list = string.split()
    lower_case_list = [word.lower() for word in as_list]

    return lower_case_list

def find_repeated(word_list):
    seen = {}
    for word in word_list:
        if seen.get(word):
            return word
        else:
            seen[word] = True
