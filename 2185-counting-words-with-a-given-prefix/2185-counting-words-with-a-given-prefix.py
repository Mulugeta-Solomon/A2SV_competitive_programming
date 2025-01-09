class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        def isPref(word) -> bool:
            if len(pref) > len(word):
                return False
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    return False
            return True

        result = 0
        for word in words:
            if isPref(word):
                result += 1
        
        return result