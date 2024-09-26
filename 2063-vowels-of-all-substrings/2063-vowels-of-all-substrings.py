class Solution:
    def countVowels(self, word: str) -> int:
        lookUp, result, curr = {'a', 'e', 'i', 'o', 'u'}, 0, 0
        
        for i, char in enumerate(word):
            if char in lookUp:
                curr += i + 1
            result += curr
        
        return result
