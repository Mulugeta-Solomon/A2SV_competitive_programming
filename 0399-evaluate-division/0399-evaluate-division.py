class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict()
        result = [-1.00000] * len(queries)

        for i in range(len(equations)):
            src, dst = equations[i]
            w = values[i]
            if src not in graph:
                graph[src] = {}
            if dst not in graph:
                graph[dst] = {}
            
            graph[src][dst] = w
            graph[dst][src] = 1 / w

        def dfs(src, dst, ans):
            # base case
            if src == dst:
                return ans 
            
            if src in visited:
                return -1 
            visited.add(src)
            
            for neighbor, w in graph[src].items():
                temp = dfs(neighbor, dst, ans * w)
                if temp != -1:
                    return temp
            
            return -1
       
        for i in range(len(queries)):
            visited = set()
            src, dst = queries[i]
            if src not in graph or dst not in graph:
                continue  
            result[i] = dfs(src, dst, 1)

        return result