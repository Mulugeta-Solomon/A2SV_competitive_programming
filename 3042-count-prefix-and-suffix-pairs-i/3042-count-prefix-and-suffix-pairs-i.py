class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return False
            i, j = len(s1) - 1, len(s2) - 1

            while i >= 0:
                if s1[i] != s2[j]:
                    return False
                i -= 1
                j -= 1
            
            return True
        
        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    result += 1

        return result 

            