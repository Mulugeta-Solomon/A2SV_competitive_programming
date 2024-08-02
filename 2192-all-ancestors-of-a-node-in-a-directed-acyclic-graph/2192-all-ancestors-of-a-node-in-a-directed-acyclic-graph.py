class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        indegree = [0] * n

        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1
        
        queue = deque()
        result = [set() for _ in range(n)]

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            size = len(queue)

            for _ in range(size):
                src = queue.popleft()
                for dst in graph[src]:
                    result[dst].add(src)
                    result[dst].update(result[src])
                    indegree[dst] -= 1
                    if indegree[dst] == 0:
                        queue.append(dst)

        result = [sorted(list(result[i])) for i in range(n)]

        return result 

