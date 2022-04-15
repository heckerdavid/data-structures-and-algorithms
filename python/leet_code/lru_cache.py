# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.
from collections import OrderedDict

class LRU:
    def __init__(self, size) -> None:
        self.size = size
        self.length = 0
        self.items = OrderedDict()

    def lru_set(self, key, value):
        if self.length >= self.size:
             k, v = self.items.popitem(last=False)
             self.items[key] = value
        else:
            self.items[key] = value
            self.length += 1

    def lru_get(self, key):
        if self.items.get(key):
            val = self.items[key]
            del self.items[key]
            self.items[key] = val
            return val

        return None
