class TrieNode:
    def __init__(self,):
        self.children = [None for _ in range(26)]
        self.is_last = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        
        curr.is_last = True

    def searchHelper(self, word: str, node):
        curr = node
        for i, char in enumerate(word):
            if char == '.':
                ans = False
                for child in curr.children:
                    if child:
                        res = self.searchHelper(word[i+1:], child)
                        if res:
                            ans = True
                return ans
            else:
                idx = ord(char) - ord('a')
                if not curr.children[idx]:
                    return False
                curr = curr.children[idx]
                
        return curr.is_last 
                
    def search(self, word: str) -> bool:
        curr = self.root

        return self.searchHelper(word, curr)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)