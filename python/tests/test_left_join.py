from left_join.left_join import left_join

def test_import():
    assert left_join


def test_left_join():
    table_1 = {'hello': "hi", 'goodbye': "bye"}
    table_2 = {'hello': "hola", 'goodbye': "adios"}


    actual = left_join(table_1, table_2)
    expected = {'hello': ["hi", "hola"], 'goodbye': ["bye", "adios"]}
    assert actual == expected

def test_left_join_offset():
    table_1 = {'hello': "hi", 'goodbye': "bye", "yes": "si"}
    table_2 = {'hello': "hola", 'goodbye': "adios"}

    actual = left_join(table_1, table_2)
    expected = {'hello': ["hi", "hola"], 'goodbye': ["bye", "adios"], "yes": ["si", None]}
    assert actual == expected

def test_left_join_no_match():
    table_1 = {'hello': "hi", 'goodbye': "bye", "yes": "si"}
    table_2 = {'hey': "hola", 'bye': "adios"}

    actual = left_join(table_1, table_2)
    expected = {'hello': ["hi", None], 'goodbye': ["bye", None], "yes": ["si", None]}
    assert actual == expected

