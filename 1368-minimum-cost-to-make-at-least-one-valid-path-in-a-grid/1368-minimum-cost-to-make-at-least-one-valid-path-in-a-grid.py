class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def get_index(x, y):
            return x * cols + y

        def in_bound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        graph = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                curr_idx = get_index(r, c)

                for i, (dr, dc) in enumerate(directions):
                    nr, nc = r + dr, c + dc
                    if in_bound(nr, nc):
                        cost = 1 if grid[r][c] != i + 1 else 0
                        graph[curr_idx].append((get_index(nr, nc), cost))
        
        costs = {node: float('inf') for node in graph}
        visited = set()
        min_heap = [(0, 0)]

        while min_heap:
            curr_cost, curr_node =  heappop(min_heap)
            if curr_node not in visited:
                visited.add(curr_node)
                
                for neighbor, neighbor_cost in graph[curr_node]:
                    cost = curr_cost + neighbor_cost
                    if cost < costs[neighbor]:
                        costs[neighbor] = cost
                        heappush(min_heap, (cost, neighbor)) 

        return costs[get_index(rows - 1, cols - 1)] if costs else 0
     