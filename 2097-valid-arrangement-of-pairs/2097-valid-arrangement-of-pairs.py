class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph  = defaultdict(list)
        indegree, outdegree = defaultdict(int), defaultdict(int)
        result = []

        for start, end in pairs:
            graph[start].append(end)
            outdegree[start] += 1
            indegree[end] += 1
                
        def dfs(curr):
            while graph[curr]:
                next_node = graph[curr].pop()
                dfs(next_node)
                result.append([curr, next_node])
        
        startNode = pairs[0][0]
        for node in outdegree:
            if outdegree[node] == indegree[node] + 1:
                startNode = node
                break
        
        dfs(startNode)

        return result [::-1]
     
