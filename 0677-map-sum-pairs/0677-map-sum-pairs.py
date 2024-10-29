class TrieNode:
    def __init__(self, val):
        self.children = [None for _ in range(26)]
        self.val = val

class Trie:
    def __init__(self):
        self.dict = TrieNode(0)
    
    def insert(self, word: str, val: int) -> None:
        curr = self.dict

        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode(0)
            curr = curr.children[idx]
            curr.val += val
    
    def search(self, prefix: str) -> int:
        curr = self.dict
        
        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return 0
            
            curr = curr.children[idx]
    
        return curr.val


class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.existed = defaultdict(int)


    def insert(self, key: str, val: int) -> None:
        currVal = val - self.existed[key]
        self.existed[key] = val
        self.trie.insert(key, currVal)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)




        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)