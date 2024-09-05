class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        
        queue, visited, result = deque(), set(), float('inf')
        queue.append(1)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                visited.add(curr)
                for neighbor, dist in graph[curr]:
                    if neighbor not in visited:
                        result = min(result, dist)
                        queue.append(neighbor)
        
        return result

        