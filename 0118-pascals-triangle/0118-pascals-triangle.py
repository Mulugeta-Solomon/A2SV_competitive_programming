class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        result = [0] * numRows
        result[0], result[1] = [1], [1, 1]

        for i in range(2, numRows):
            curr = [0] * (i + 1)
            curr[0] = curr[-1] = 1
            for j in range(1, i):
                curr[j] = result[i-1][j-1] + result[i-1][j] 
            
            result[i] = curr
        
        return result
