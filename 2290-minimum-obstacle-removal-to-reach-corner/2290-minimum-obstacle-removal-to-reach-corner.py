class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        graph, directions = defaultdict(list), [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])

        def idx(row, col, column=m):
            return (row * column) + col

        for row in range(n):
            for col in range(m):
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if 0 <= newRow < n and 0 <= newCol < m:
                        graph[(idx(row, col))].append((idx(newRow, newCol), grid[newRow][newCol]))

        def dijkstra(graph, start=0):
            distances = {node: float('inf') for node in range(m * n)}
            distances[start] = 0

            heap, visited = [(0, start)], set()

            while heap:
                curr_distance, curr_node = heappop(heap)

                if curr_node not in visited:
                    visited.add(curr_node)

                    for neighbor, weight in graph[curr_node]:
                        distance = curr_distance + weight
                        if distance < distances[neighbor]:
                            distances[neighbor] = distance 
                            heappush(heap, (distance, neighbor))
            
            return distances[(n * m) - 1]

        return  dijkstra(graph)
