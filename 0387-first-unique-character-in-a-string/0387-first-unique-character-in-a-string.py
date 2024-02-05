class Solution:
    def firstUniqChar(self, s: str) -> int:

        look_up = {}

        for idx, letter in enumerate(s):
            if letter not in look_up:
                look_up[letter] = 0 
            else:
                look_up[letter] += 1
        

        for letter, idx in look_up.items():
            if idx == 0:
                return s.index(letter)

        return -1 
    
        