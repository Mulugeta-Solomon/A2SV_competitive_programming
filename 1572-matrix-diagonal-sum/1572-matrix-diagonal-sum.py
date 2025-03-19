class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result, n = 0, len(mat)
        
        for i in range(n):
            result += (mat[i][i] + mat[i][n - i - 1])
        if n % 2:
            return result - mat[n // 2][n // 2]
        
        return result
        