from CodeFellows401.stack_queue_brackets.validate_brackets import validate_brackets

def test_import():
    assert validate_brackets

def test_valid_round_brackets():
    assert validate_brackets('()')

def test_valid_brackets():
    assert validate_brackets('{}(){}')
    assert validate_brackets('(){}[[]]')
    assert validate_brackets('[[({})]]')
    assert validate_brackets('{}{Code}[Fellows](())')

def test_invalid_brackets():
    assert not validate_brackets('[({}]')
    assert not validate_brackets('(](')
    assert not validate_brackets('{({})})}]')

def test_imbedded():
    assert validate_brackets('[({})]')

def test_out_of_order():
    assert not validate_brackets('][')
