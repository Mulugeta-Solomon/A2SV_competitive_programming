class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)

        curr_row_sum = [0] * n
        curr_col_sum = [0] * m

        result = [[0] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                result[r][c] = min(rowSum[r] - curr_row_sum[r], colSum[c] - curr_col_sum[c])
                curr_row_sum[r] += result[r][c]
                curr_col_sum[c] += result[r][c]
        
        return result
