from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # initialize the LRUCache object with a specific capacity
        # parameter: capacity (int), the maximum number of key-value pairs the cache can hold
        self.capacity = capacity
        # using OrderedDict to maintain the order of insertion
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # retrieve the value associated with the given key from the cache
        # parameter: key (int), the key whose value needs to be retrieved
        # return: the value associated with the key, or -1 if the key is not present 
        # in the cache
        if key not in self.cache:
            return -1
        # move the accessed key to the end to indicate it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # insert or update the value associated with the given key in the cache
        # if the key is already present, update its value and move it to the end to indicate
        # it was recently used
        # if the key is not present and the cache is full, remove the least recently used 
        # key-value pair before inserting the new one.
        # parameters: 1. key (int), The key to be inserted or updated 
        #             2. value (int), The value associated with the key
        if key in self.cache:
            # if the key already exists, move it to the end
            self.cache.move_to_end(key)
        # update the value or insert the new key-value pair
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # if the cache exceeds its capacity, remove the least recently used key-value pair
            self.cache.popitem(last = False)

if __name__ == '__main__':
    myLRUCache = LRUCache(2)
    myLRUCache.put(1,1)
    myLRUCache.put(2,2)
    print('get:', myLRUCache.get(1))
    myLRUCache.put(3,3)
    print('get:', myLRUCache.get(2))
    myLRUCache.put(4,4)
    print('get:', myLRUCache.get(1))
    print('get:', myLRUCache.get(3))
    print('get:', myLRUCache.get(4))