class HashTable():

    def __init__(self) -> None:
        self.length = 701

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
