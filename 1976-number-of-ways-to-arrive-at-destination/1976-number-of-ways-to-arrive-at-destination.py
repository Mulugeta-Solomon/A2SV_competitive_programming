class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 1
        graph = defaultdict(list)
        for u, v, weight in roads:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        min_heap, distance, path = [(0, 0)], [float('inf')] * n, [0] * n
        distance[0], path[0] = 0, 1 

        while min_heap:
            size = len(min_heap)
            for _ in range(size):
                curr_time, node = heappop(min_heap)
                if curr_time > distance[node]:
                    continue

                for neighbor, time in graph[node]:
                    if curr_time + time < distance[neighbor]:
                        distance[neighbor] = curr_time + time
                        path[neighbor] = path[node]
                        heappush(min_heap, (curr_time + time, neighbor))
                    elif curr_time + time == distance[neighbor]:
                        path[neighbor] = (path[neighbor] + path[node]) % MOD
        
        return path[n - 1]
        
