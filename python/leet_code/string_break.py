# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

def word_break(string, word_dict):

    min_length = float('inf')
    max_length = float('-inf')
    for item in word_dict:
        min_length = min(min_length, len(item))
        max_length = max(max_length, len(item))

    left = 0
    right = min_length

    sentence_list = []
    longest_valid = ''

    while left < len(string) - 1:
        sub_string = string[left:right]
        if sub_string in word_dict:
            longest_valid = sub_string
            end_point = right
        if right - left <= max_length:
            right += 1
        else:
            left = end_point
            right = left + min_length
            sentence_list.append(longest_valid)
            longest_valid = ''

    return sentence_list
