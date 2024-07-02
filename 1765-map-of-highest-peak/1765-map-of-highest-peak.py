class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows, cols = len(isWater), len(isWater[0])
        
        def isInbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    queue.append((r, c, 0))
        
        heights = [[-1 for _ in range(rows)] for _ in range(cols)]
        visited = set()
        while queue:
            size = len(queue)

            for _ in range(size):
                r, c, curr = queue.popleft()

                if (r,c) not in visited and heights[r][c] == -1:
                    heights[r][c] = curr
                    visited.add((r, c))
                    for direction in directions:
                        newRow, newCol = r + direction[0], c + direction[1]
                        if isInbound(newRow, newCol) and (newRow, newCol) not in visited and heights[newRow][newCol] == -1:
                            queue.append((newRow, newCol, curr + 1))


        return heights