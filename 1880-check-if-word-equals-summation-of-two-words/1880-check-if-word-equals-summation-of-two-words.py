class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def wordTonum(s):
            num = ''
            for char in s:
                num += str(ord(char) - 97)
            
            return int(num)
        
        if wordTonum(firstWord) + wordTonum(secondWord) == wordTonum(targetWord):
            return True
        
        return False