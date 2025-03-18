class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist1, dist2 = [-1] * (n + 1), [-1] * (n + 1)
        queue = deque([(1, 1)])
        dist1[1] = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node, freq = queue.popleft()
                curr_time = dist1[node] if freq == 1 else dist2[node]

                if (curr_time // change) % 2 == 1:
                    curr_time = change * (curr_time // change + 1) + time
                else:
                    curr_time = curr_time + time
                
                for neighbor in graph[node]:
                    if dist1[neighbor] == -1:
                        dist1[neighbor] = curr_time
                        queue.append((neighbor, 1))
                    elif dist2[neighbor] == -1 and dist1[neighbor] != curr_time:
                        if neighbor == n:
                            return curr_time
                        dist2[neighbor] = curr_time
                        queue.append((neighbor, 2))
        