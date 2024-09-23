class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        result = []

        for word in words:
            dic = {}
            visited = set()

            for i, char in enumerate(word):
                if pattern[i] not in visited:
                    dic[char] = pattern[i]
                    visited.add(pattern[i])
            
            check = ''

            for i, char in enumerate(word):
                if char in dic:
                    check += dic[char]
            
            if check == pattern:
                result.append(word)
        
        return result
