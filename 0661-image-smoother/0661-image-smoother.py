class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for row in range(len(img)):
            for col in range(len(img[0])):

                surr_idxs = [(row, col), (row-1, col), (row+1, col), 
                            (row, col-1), (row, col+1), (row-1, col-1), 
                            (row+1, col+1), (row-1, col+1), (row+1, col-1)]
                
                current_sum = 0
                idx_counter = 0
                for idx in surr_idxs:
                    r, c = idx

                    if r >= 0 and c >= 0 and r < m and c < n:
                        current_sum += img[r][c]
                        idx_counter += 1

                result[row][col] = current_sum // idx_counter

        return result

        