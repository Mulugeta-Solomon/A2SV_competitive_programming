class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        graph = {1: ((0, -1), (0, 1)), 
                 2: ((-1, 0), (1, 0)), 
                 3: ((0, -1), (1, 0)),
                 4: ((0, 1), (1, 0)), 
                 5: ((0, -1), (-1, 0)),
                 6: ((0, 1), (-1, 0)) }

        def isInbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            # Base case
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True
            visited.add((row, col))
            for r, c in graph[grid[row][col]]:
                newRow, newCol = row + r, col + c
                if isInbound(newRow, newCol) and (newRow, newCol) not in visited:
                    if (-r, -c) in graph[grid[newRow][newCol]]: # check that next cell does connect to the current
                        if dfs(newRow, newCol):
                            return True
            
            return False
        visited = set()
        return dfs(0, 0)