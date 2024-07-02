class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = [[False] * 2 for _ in range(n)]

        for i in range(len(redEdges)):
            u, v = redEdges[i]
            graph[u].append([v, 0])
        
        for i in range(len(blueEdges)):
            u, v  = blueEdges[i]
            graph[u].append([v, 1])
        
        result = [-1] * n
        result[0] = 0
        visited[0][0] = visited[0][1] = True
        queue = deque([(0, -1)])
        distance = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node, prev_color = queue.popleft()

                for neighbor, color in graph[node]:
                    if not visited[neighbor][color] and prev_color != color:
                        if result[neighbor] == -1:
                            result[neighbor] = distance + 1
                        
                        visited[neighbor][color] = True
                        queue.append((neighbor, color))
            distance += 1

        return result

