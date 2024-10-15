class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        nums, result =[[0] * n for _ in range(m)], 0

        for r, c in indices:
            for i in range(n):
                nums[r][i] += 1
            for j in range(m):
                nums[j][c] += 1

        for i in range(m):
            for j in range(n):
                if nums[i][j] % 2 != 0:
                    result += 1
        
        return result