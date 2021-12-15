from stack_queue_brackets.validate_brackets import validate_brackets

def test_import():
    assert validate_brackets

def test_valid_round_brackets():
    assert validate_brackets('()')

def test_valid_brackets():
    assert validate_brackets('{}(){}')
    assert validate_brackets('(){}[[]]')
    assert validate_brackets('{}{Code}[Fellows](())')

def test_invalid_brackets():
    assert not validate_brackets('[({}]')
    assert not validate_brackets('(](')
    assert not validate_brackets('{({})})}]')
