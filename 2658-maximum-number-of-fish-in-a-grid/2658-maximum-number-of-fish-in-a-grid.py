class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        result, visited = float('-inf'), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    queue, curr_sum = deque([(i, j)]), 0
                    while queue:
                        size = len(queue)
                        for _ in range(size):
                            r, c = queue.popleft()
                            visited.add((r, c))
                            curr_sum += grid[r][c]

                            for dr, dc in directions:
                                nr, nc = r + dr, c + dc
                                if inbound(nr, nc) and grid[nr][nc] > 0 and (nr, nc) not in visited:
                                    queue.append((nr, nc))

                    result = max(result, curr_sum)
        
        return max(result, 0)

        