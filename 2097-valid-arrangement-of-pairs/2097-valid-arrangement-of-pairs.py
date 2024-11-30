class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph  = defaultdict(deque)
        indegree, outdegree = defaultdict(int), defaultdict(int)
        result, startNode = [], -1

        for start, end in pairs:
            graph[start].append(end)
            outdegree[start] += 1
            indegree[end] += 1
                
        def dfs(node):
            while graph[node]:
                next_node = graph[node].popleft()
                dfs(next_node)
            
            result.append(node)
        
        for node in outdegree:
            if outdegree[node] == indegree[node] + 1:
                startNode = node
                break
        
        if startNode == -1:
            startNode = pairs[0][0]
        
        dfs(startNode)
        result = result[::-1]

        return [[result[i-1], result[i]] for i in range(1, len(result))]


        
