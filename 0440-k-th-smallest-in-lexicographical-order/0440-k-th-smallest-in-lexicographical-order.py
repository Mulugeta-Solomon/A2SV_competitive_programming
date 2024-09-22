class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        result = []
        def dfs(num):
            if num > n:
                return
            result.append(num)
            num *= 10

            for i in range(10):
                dfs(num + i)

        for i in range(1, 10):
            dfs(i)

        return result[k - 1]
