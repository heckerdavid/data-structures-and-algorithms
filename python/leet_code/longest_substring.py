# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

#  N ^ 2 method
def max_substring(string, K):
    max_length = 0

    for idx, val in enumerate(string):
        seen = set()
        seen.add(val)
        next_idx = idx + 1
        current_length = 1

        while next_idx <= len(string)-1:
            if string[next_idx] not in seen:
                seen.add(string[next_idx])

            if len(seen) <= K:
                current_length += 1
            next_idx += 1

        if current_length > max_length:
            max_length = current_length


    return max_length

#  TODO: sliding window O(n) method
