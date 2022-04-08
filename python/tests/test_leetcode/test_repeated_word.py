from hash_table.repeated_word.repeatedword import repeated_word, convert_str_to_list, find_repeated

def test_import():
    assert convert_str_to_list

def test_string_to_list():
    string = "Hello; my. name's Python!"
    actual = convert_str_to_list(string)
    expected = ['hello', 'my', 'names', 'python']
    assert actual == expected


def test_string_to_list_case_2():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."

    actual = convert_str_to_list(string)
    expected = ['it', 'was', 'a', 'queer', 'sultry', 'summer', 'the', 'summer', 'they', 'electrocuted', 'the', 'rosenbergs', 'and', 'i', 'didnt', 'know', 'what', 'i', 'was', 'doing', 'in', 'new', 'york']
    assert actual == expected

def test_find_repeated():
    words = ['hello', 'my', 'names', 'python', 'my']

    actual = find_repeated(words)
    expected = 'my'
    assert actual == expected

def test_find_repeated_case_2():
    words = ['it', 'was', 'a', 'queer', 'sultry', 'summer', 'the', 'summer', 'they', 'electrocuted', 'the', 'rosenbergs', 'and', 'i', 'didnt', 'know', 'what', 'i', 'was', 'doing', 'in', 'new', 'york']

    actual = find_repeated(words)
    expected = 'summer'
    assert actual == expected


def test_repeated_word_case_1():
    string = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(string)
    expected = 'a'
    assert actual == expected

def test_repeated_word_case_2():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(string)
    expected = 'it'
    assert actual == expected

def test_repeated_word_case_3():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."
    actual = repeated_word(string)
    expected = 'summer'
    assert actual == expected
