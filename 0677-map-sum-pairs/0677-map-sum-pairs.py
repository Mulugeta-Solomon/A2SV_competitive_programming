# class TrieNode:
#     def __init__(self, ):
#         self.children = {}
#         self.is_last = False

class MapSum:

    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        curr = self.trie
        curr[key] = val


    def sum(self, prefix: str) -> int:
        result = 0
        for key in self.trie:
            flag = True
            if len(key) < len(prefix):
                continue
            for i, char in enumerate(prefix):
                if char != key[i]:
                    flag = False
                    break
            if flag:
                result += self.trie[key]
        
        return result 




        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)