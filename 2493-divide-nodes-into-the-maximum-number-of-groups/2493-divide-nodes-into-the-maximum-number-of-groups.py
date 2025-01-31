class Solution:
    def magnificentSets(self, n, edges):
        adj = [[] for _ in range(n)] # collect connected nodes for each node
        for node1, node2 in edges:
            adj[node1-1].append(node2-1)
            adj[node2-1].append(node1-1)

        # bipartite check to ensure each node can be divided into at least 2 groups, one for each color
        color = [0] * n # no starting color
        for node in range(n):
            if color[node] != 0: continue
            color[node] = 1 # give node the default color
            queue = deque([node])

            while queue: # explore connected nodes and color
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if color[neighbor] == color[curr]: 
                        return -1 # if connected nodes are same color, graph isn't bipartite
                    if color[neighbor] == 0:
                        color[neighbor] = -color[curr] # give connected node opposite color
                        queue.append(neighbor) # check connected node
        
        def find_depth(root): # bfs, get depth of tree starting at root
            visited = [False] * n
            visited[root] = True
            queue = deque([root])
            distance = 0
            while queue:
                for _ in range(len(queue)): # add all connected nodes to queue
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                distance += 1 # explored all connected nodes, go to next layer
            return distance

        def find_max_depth(node): # dfs, find max depth for tree that contains node
            visited[node] = True
            max_dist = distances[node]
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    max_dist = max(max_dist, find_max_depth(neighbor))
            return max_dist

        distances = [find_depth(node) for node in range(n)] # depth for each tree starting at node
        visited = [False] * n # memo for find_max_depth, only need to check each node once
        groups = 0
        for node in range(n):
            if not visited[node]:
                groups += find_max_depth(node)

        return groups