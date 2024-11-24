class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result, negCount, min_val, n = 0, 0, float('inf'), len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negCount += 1
                result += abs(matrix[i][j])
                min_val = min(min_val, abs(matrix[i][j]))
        
        if negCount % 2 == 1:
            result -= (2 * min_val)
        
        return result