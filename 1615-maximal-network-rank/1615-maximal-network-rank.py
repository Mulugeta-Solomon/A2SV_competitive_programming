class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
    
        graph = defaultdict(list)

        for road in roads:
            a, b = road
            graph[a].append(b)
            graph[b].append(a)

        max_network = float('-inf') 
        for i in range(n):
            for j in range(i + 1, n):

                if i in graph[j] and j in graph[i]:
                    max_network = max(max_network, len(graph[i]) + len(graph[j]) - 1)
                else:
                    max_network = max(max_network, len(graph[i]) + len(graph[j]))
        
        return max_network


