class TrieNode:
    def __init__(self,):
        self.children = [None for _ in range(26)]
        self.is_last = False

class Trie:

    def __init__(self):
        self.node = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.node
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_last = True 

    def search(self, word: str) -> bool:
        curr = self.node
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        
        return curr.is_last

    def startsWith(self, prefix: str) -> bool:
        curr = self.node 
        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)