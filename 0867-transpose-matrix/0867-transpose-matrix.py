class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row, column = len(matrix), len(matrix[0])
        transposed_matrix = [[0 for _ in range(row)] for _ in range(column)]

        for i in range(column):
            for j in range(row):
                transposed_matrix[i][j] = matrix[j][i] 
        
        return transposed_matrix

        