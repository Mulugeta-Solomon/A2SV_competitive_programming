class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[float('inf')] * n for _ in range(n)]
        memo[-1] = matrix[-1]

        for row in range(n - 2, -1, -1):
            for col in range(n):
                memo[row][col] = matrix[row][col] + min(memo[row + 1][col], 
                                 memo[row + 1][col - 1] if col > 0 else float('inf'), 
                                 memo[row + 1][col + 1] if col < n - 1 else float('inf'))
        return min(memo[0])