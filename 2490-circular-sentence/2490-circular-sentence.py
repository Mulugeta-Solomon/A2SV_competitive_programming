class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence[0] == sentence[-1]:
            return False
        sentence = sentence.split(' ')
        
        for i in range(len(sentence) - 1):
            if not sentence[i][-1] == sentence[i+1][0]:
                return False

        return True