class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row, col, result = len(grid), len(grid[0]), [0] * len(queries)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort(key = lambda x:x[0])

        def inbound(x, y):
            return 0 <= x < row and 0 <= y < col

        heap, visited, count = [], set(), 0
        heappush(heap, (grid[0][0], 0, 0))
        visited.add((0, 0))

        for curr, idx in queries:
            while heap and heap[0][0] < curr:
                val, r, c = heappop(heap)
                count += 1
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heappush(heap, (grid[nr][nc], nr, nc))
            
            result[idx] = count

        return result
