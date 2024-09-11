class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        xor = start ^ goal

        while xor != 0:
            result += xor & 1
            xor >>= 1

        return result 
        