class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        result = 0
        
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    break
                if i == len(word) - 1:
                    result += 1
        
        return result 