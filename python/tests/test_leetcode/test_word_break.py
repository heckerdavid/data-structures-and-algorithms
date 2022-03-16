from leet_code.string_break import word_break

def test_import():
    assert word_break

def test_word_break_qbf():
    string = "thequickbrownfox"
    word_set = set(['quick', 'brown', 'the', 'fox'])

    actual = word_break(string, word_set)
    expected = ['the', 'quick', 'brown', 'fox']
    assert actual == expected

def test_word_break_bbby():
    string = "bedbathandbeyond"
    word_set = set(['bed', 'bath', 'bedbath', 'and', 'beyond',])

    actual = word_break(string, word_set)
    expected = ['bedbath', 'and', 'beyond']
    alt_expected = ['bed', 'bath', 'and', 'beyond']
    assert actual == expected or actual == alt_expected

def test_word_break_imbedded_words():
    string = "thereistheisotope"
    word_set = set(['there', 'isotope', 'is', 'top', 'the'])

    actual = word_break(string, word_set)
    expected = ['there', 'is', 'the', 'isotope']
    assert actual == expected
