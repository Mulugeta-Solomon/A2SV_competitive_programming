class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        terminal = set()
        indegree = [0] * len(graph)
        ans = []
        rev_graph = defaultdict(list) # reverse the graph to get the current terminal 

        for i in range(len(graph)):
            # if len(graph[i]) == 0: # outdegree = 0
            #     terminal.add(i)
            #     ans.add(i)
            
            for src in graph[i]:
                rev_graph[src].append(i)
                indegree[i] += 1

        queue = deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                ans.append(node)

                for dst in rev_graph[node]:
                    indegree[dst] -= 1
                    if indegree[dst] == 0:
                        queue.append(dst) # append safe nodes

            
        return sorted(ans)


