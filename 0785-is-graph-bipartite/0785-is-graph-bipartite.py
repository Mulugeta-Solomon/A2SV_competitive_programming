class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(node, color):
            if colors[node] != 0:
                return colors[node] == color
            
            colors[node] = color

            for neighbor in graph[node]:
                if not dfs(neighbor, -color):
                    return False
            
            return True

        colors = [0] * len(graph)

        for i in range(len(graph)):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
               
        return True