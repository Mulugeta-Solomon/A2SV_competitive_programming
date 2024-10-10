class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        result = [0] * k
        i, j = 1, 0

        while i <= n:
            if n % i == 0:
                result[j] = i
                j += 1

            i += 1

            if result[-1] != 0:
                return result[-1]

        if result[-1] != 0:
            return result[-1]
        return -1
