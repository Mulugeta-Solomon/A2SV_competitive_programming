class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for _ in range(rows)]
        heap, result = [], 0 # min-heap

        def inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        # Boundary
        for r in range(rows):
            heappush(heap, (heightMap[r][0], r, 0))
            heappush(heap, (heightMap[r][cols - 1], r, cols - 1))
            visited[r][0] = visited[r][cols - 1] = True
        
        for c in range(1, cols - 1):
            heappush(heap, (heightMap[0][c], 0, c))
            heappush(heap, (heightMap[rows - 1][c], rows - 1, c))
            visited[0][c] = visited[rows - 1][c] = True
        
        max_height = 0
        while heap:
            curr_height, r, c = heappop(heap)
            max_height = max(max_height, curr_height)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if heightMap[nr][nc] < max_height:
                        result += (max_height - heightMap[nr][nc])
                    heappush(heap, (max(max_height, heightMap[nr][nc]), nr, nc))
        
        return result

