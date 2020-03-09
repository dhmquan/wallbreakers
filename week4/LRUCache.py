#from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = []
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        #update this key to front of q
        pos_in_q = self.q.index(key)
        del self.q[pos_in_q]
        self.q.insert(0, key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        #first check if the key is already in dict
        if key in self.dict:
            pos_in_q = self.q.index(key)
            del self.q[pos_in_q]
        
        #next check for dict capacity
        elif len(self.q) >= self.capacity:
            evicted_key = self.q.pop()
            del self.dict[evicted_key]

        self.q.insert(0, key)
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)