class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra(graph, start):
            distances = [float('inf')] * n
            distances[start] = 0
            visited = set()

            heap = [(0, start)]

            while heap:
                curr_distance, curr_city = heappop(heap)
                if curr_city not in visited:
                    visited.add(curr_city)

                    for neighbor in graph[curr_city]:
                        distance = curr_distance + 1
                        if distance < distances[neighbor]:
                            distances[neighbor] = distance 
                            heappush(heap, (distance, neighbor))
            
            return distances[n - 1] 
        
        graph, result = {city: [] for city in range(n)}, [0] * len(queries)

        for city in range(n - 1):
            graph[city].append(city + 1)

        for i, (u, v) in enumerate(queries):
            graph[u].append(v)
            shortest_dist = dijkstra(graph, 0)
            result[i] = shortest_dist
        
        return result 