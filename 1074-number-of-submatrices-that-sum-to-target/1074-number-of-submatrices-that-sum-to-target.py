class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                prefix_sum[row][col] = matrix[row-1][col-1] + prefix_sum[row-1][col] \
                                       + prefix_sum[row][col-1] - prefix_sum[row-1][col-1]
        print(prefix_sum)
        count = 0

        for start_row in range(rows):
            for end_row in range(start_row, rows):
                look_up = {0: 1}

                for col in range(cols):
                    curr_sum = prefix_sum[end_row + 1][col + 1] - prefix_sum[start_row][col + 1]
                    
                    if curr_sum - target in look_up:
                        count += look_up[curr_sum - target]

                    look_up[curr_sum] = look_up.get(curr_sum, 0) + 1
        
        return count
