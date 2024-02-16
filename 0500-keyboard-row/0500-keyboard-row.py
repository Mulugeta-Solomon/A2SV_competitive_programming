class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1, row2, row3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"

        result = []
        for word in words:
            if len(set(word.lower() + row1)) == len(set(row1)) or len(set(word.lower() + row2)) == len(set(row2)) or len(set(word.lower() + row3)) == len(set(row3)):
                result.append(word)
        
        return result

        