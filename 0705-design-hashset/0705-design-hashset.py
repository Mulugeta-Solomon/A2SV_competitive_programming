class MyHashSet:

    def __init__(self):
        self.key = [0] * (10**6 + 1)
        
    def add(self, key: int) -> None:
        self.key[key] = 1

    def remove(self, key: int) -> None:
        self.key[key] = 0

    def contains(self, key: int) -> bool:
        return self.key[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)