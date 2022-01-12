class HashTable():

    def __init__(self) -> None:
        self.length = 701
        self.table = [[]] * self.length

    def hash(self, key) -> int:

        if type(key) is str:
            hash_key = self.convert_str_to_int(key)
        elif type(key) is int:
            hash_key = key

        index = (hash_key * 7717) % self.length

        return index

    def convert_str_to_int(self, string):
        ascii_values = [ord(letter) for letter in string]

        return sum(ascii_values)

    def add(self, key, value) -> None:
        hash_key = self.hash(key)

        index_inner_list = self.table[hash_key]

        index_inner_list.append((key, value))

    def get(self, key) -> any:
        hash_key = self.hash(key)

        index_inner_list = self.table[hash_key]

        if len(index_inner_list) == 0:
            return None
        else:
            for pair in index_inner_list:
                if pair[0] == key:
                    return pair[1]
        return None

    def contains(self, key):
        return bool(self.get(key))

    def remove(self, key):
        hash_key = self.hash(key)

        index_inner_list = self.table[hash_key]


        if len(index_inner_list) == 1:
            return_value = index_inner_list[0][1]
            self.table[hash_key] = []
        elif len(index_inner_list) == 0:
            return_value =  f' {key} not in hash table'
        else:
            for pair in index_inner_list:
                if pair[0] == key:
                    return_value = pair[1]
                    index_inner_list.remove(pair)

        return return_value
