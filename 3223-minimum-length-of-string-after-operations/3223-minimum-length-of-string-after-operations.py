class Solution:
    def minimumLength(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        result = 0
        for char, val in freq.items():
            if val % 2 == 0:
                result += 2
            else:
                result += 1
        
        return result