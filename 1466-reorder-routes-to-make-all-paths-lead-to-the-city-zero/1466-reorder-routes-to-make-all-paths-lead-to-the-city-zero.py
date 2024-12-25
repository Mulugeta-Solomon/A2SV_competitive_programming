class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited, result = set(), [0]

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, -1))

        def dfs(node: int):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor[0] not in visited:
                    if neighbor[1] == 1:
                        result[0] += 1
                    dfs(neighbor[0])

        dfs(0)

        return result[0]
                