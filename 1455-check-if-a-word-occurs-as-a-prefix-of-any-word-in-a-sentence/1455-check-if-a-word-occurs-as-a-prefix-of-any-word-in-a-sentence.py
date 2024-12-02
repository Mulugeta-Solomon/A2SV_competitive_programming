class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = list(sentence.split(' '))
        
        for i, word in enumerate(words):
            left, right, idx = 0, 0, 0
            
            while right < len(word):
                if word[left:right + 1] == searchWord:
                    return i + 1
                if word[right] == searchWord[idx]:
                    right += 1
                    idx += 1
                    continue               
                break
        
        return -1

                
