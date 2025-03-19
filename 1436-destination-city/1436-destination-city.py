class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(int)
        result = [] 
        for u, v in paths:
            result.extend([u, v])
            graph[u] += 1
        
        for city in result:
            if not graph[city]:
                return city