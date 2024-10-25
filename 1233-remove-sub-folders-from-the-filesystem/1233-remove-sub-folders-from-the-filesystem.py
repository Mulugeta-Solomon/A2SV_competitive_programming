class TrieNode:
    def __init__(self,):
        self.children = {}
        self.is_last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        curr = self.root
        for char in word.split('/')[1:]:
            if curr.is_last:
                break
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_last = True

        #     if char != '/':
        #         # idx = ord(char) - ord('a')
        #         if curr.is_last:
        #             break
        #         if not curr.children[char]:
        #             curr.children[char] = TrieNode()
        #         curr = curr.children[idx]
        # curr.is_last = True
    
    def build(self,) -> List[int]:
        result = []

        def backtrack(root, curr):
            if root.is_last:
                result.append(curr[:])
                return 
            
            for char, children in root.children.items():
                curr += '/' + char
                backtrack(children, curr)
                curr = curr[:-(len(char) + 1)]

        
        backtrack(self.root, '')

        return result


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for path in folder:
            trie.insert(path)
        
        return trie.build()
