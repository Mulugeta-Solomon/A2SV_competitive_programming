class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        fresh_oranges = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                
                fresh_oranges += grid[row][col] == 1
        
        minutes = 0

        while queue:
            size = len(queue)

            if fresh_oranges == 0:
                return minutes

            for _ in range(size):
                row, col = queue.popleft()
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]

                    if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2 # Mark visited
                        fresh_oranges -= 1
            minutes += 1

        return minutes if fresh_oranges == 0 else -1  
