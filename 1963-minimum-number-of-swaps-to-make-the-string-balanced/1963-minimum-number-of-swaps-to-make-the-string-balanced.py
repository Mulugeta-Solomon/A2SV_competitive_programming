class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0

        for br in s:
            if br == '[':
                swaps += 1
            elif swaps > 0:
                swaps -= 1
        
        return (swaps + 1) // 2

        