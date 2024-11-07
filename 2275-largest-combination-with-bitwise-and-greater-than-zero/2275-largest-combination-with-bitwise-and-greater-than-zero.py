class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        result = 0
        for i in range(24):
            curr = 0
            for candidate in candidates:
                bits = bin(candidate)[2:]
                if i < len(bits) and bits[len(bits) - i - 1] == '1':
                    curr += 1
            result = max(result, curr)

        return result