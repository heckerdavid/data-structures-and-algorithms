# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

# TODO: Fix end point break
def encode_string(string):
    left_index = 0
    right_index = 0
    encoded_string = ''

    while right_index < len(string) - 1:

        while string[left_index] == string[right_index] and right_index < len(string) - 1:
            right_index += 1

        encoded_string += str(right_index - left_index)
        encoded_string += string[left_index]
        left_index = right_index
        right_index += 1


    return encoded_string
