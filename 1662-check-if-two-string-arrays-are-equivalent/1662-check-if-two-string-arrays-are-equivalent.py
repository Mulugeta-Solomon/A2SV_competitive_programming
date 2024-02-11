class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        word1 = ''.join(word1)
        word2 = ''.join(word2)
        i = 0
        for char in word1:
            if char != word2[i] or len(word1) != len(word2):
                return False
            i += 1
        
        return True


        