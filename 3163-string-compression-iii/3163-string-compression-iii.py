class Solution:
    def compressedString(self, word: str) -> str:
        
        result, curr, count = '', word[0], 0

        for i in range(len(word)):
            if curr == word[i] and count < 9:
                count += 1
            else:
                result += str(count) + curr
                curr = word[i]
                count = 1
            
            if i == len(word) - 1:
                result += str(count) + curr 
        
        return result