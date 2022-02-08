def left_join(table_1, table_2):
    return_table = {}

    for key, val in table_1.items():
        if table_2.get(key):
            return_table[key] = [val, table_2.get(key)]

        else:
            return_table[key] = [val, None]

    return return_table
