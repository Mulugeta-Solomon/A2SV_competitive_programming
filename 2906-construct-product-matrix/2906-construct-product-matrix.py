class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n, m = len(grid), len(grid[0])

        result =[[1] * m for _ in range(n)]

        forward, backward = 1, 1

        for row in range(n):
            for col in range(m):
                result[row][col] = forward
                forward = (forward * grid[row][col]) % 12345 

        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                result[row][col] = (result[row][col] * backward) % 12345
                backward = (backward * grid[row][col]) % 12345
        
        return result