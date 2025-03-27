class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        maxx = [0] * len(matrix[0])
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                maxx[i] = max(maxx[i], matrix[j][i])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = maxx[j]
        
        return matrix