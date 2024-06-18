class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            src, dest = edge
            graph[src].append(dest) 
            graph[dest].append(src) 

        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False 
            
        visited = set()  
        return dfs(source, visited)
