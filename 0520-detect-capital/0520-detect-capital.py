class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        if word[0] == word[0].upper():
            return word[1:].islower() 
        
        return False