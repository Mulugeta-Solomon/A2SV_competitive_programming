class Solution:
    def reverseVowels(self, s: str) -> str:
        
        lookUp = {'a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U'}
        word = list(s)
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and word[left] not in lookUp:
                left += 1
            
            while left < right and word[right] not in lookUp:
                right -= 1

            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        
        result = ''.join(word)
        
        return result
        
        
        



        