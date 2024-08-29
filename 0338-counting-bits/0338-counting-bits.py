class Solution:
    def countBits(self, n: int) -> List[int]:

        result = []

        for num in range(n + 1):
            result.append(num.bit_count())
        
        return result
        