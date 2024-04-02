class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])
        prefix_sum = [[0] * m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                prefix_sum[row][col] = prefix_sum[row-1][col if row else 0] + (prefix_sum[row][col-1] if col else 0) - (prefix_sum[row-1][col-1] if row and col else 0) + mat[row][col]
      
        for row in range(n):
            for col in range(m):
                mat[row][col] = prefix_sum[min(row+k, m-1)][min(col+k,n-1)] - (prefix_sum[min(m-1,row+k)][col-k-1] if col>k else 0) - (prefix_sum[row-k-1][min(col+k,n-1)] if row>k else 0) + (prefix_sum[row-k-1][col-k-1] if row>k and col>k else 0 )    
       
        return mat