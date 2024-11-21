class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        directions, total =[(1, 0), (-1, 0), (0, 1), (0, -1)], len(guards) + len(walls) 

        for row, col in guards + walls:
            grid[row][col] = -1
        
        for gx, gy in guards:
            for x, y in directions:
                row, col = gx, gy
                while 0 <= row + x < m and 0 <= col + y < n and grid[row + x][col + y] != -1:
                    row += x
                    col += y
                    if grid[row][col] == 0:
                        grid[row][col] = 1
                        total += 1
        
        return (n * m) - total


        
