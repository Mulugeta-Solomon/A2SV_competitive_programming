class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_reachable = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        result, graph = [None] * len(queries), defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
    
        for i in range(numCourses):
            queue = deque([i])
            while queue:
                size = len(queue)
                for _ in range(size):
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if not is_reachable[curr][neighbor]:
                            is_reachable[i][neighbor] = True
                            queue.append(neighbor)
        
        for i, (u, v) in enumerate(queries):
            result[i] = is_reachable[u][v]
        
        return result
