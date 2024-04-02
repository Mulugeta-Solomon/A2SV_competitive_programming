class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        
        self.prefix_sum_mat = [[0] * (m+1) for i in range(n+1)]

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                self.prefix_sum_mat[row][col] = self.prefix_sum_mat[row-1][col] + self.prefix_sum_mat[row][col-1]  - self.prefix_sum_mat[row-1][col-1] + matrix[row-1][col-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum_mat[row2+1][col2+1] - self.prefix_sum_mat[row2+1][col1] - self.prefix_sum_mat[row1][col2+1] + self.prefix_sum_mat[row1][col1]

'''
        bottomRight = self.sumMat[row2+1][col2+1]
        above = self.sumMat[row1][col2+1]
        left = self.sumMat[row2+1][col1]
        topLeft = self.sumMat[row1][col1]
        
        return bottomRight - above - left + topLeft 
'''

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)