class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1

        def backtrack(node, path):
            if path[-1] == n:
                result.append(path[:])
                return 

            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
        
        result = []
        backtrack(0, [0])
        return result