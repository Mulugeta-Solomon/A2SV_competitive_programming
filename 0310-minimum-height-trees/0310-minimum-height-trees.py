class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        tree, degrees = [[] for _ in range(n)], [0] * n

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        queue, remaining = deque([i for i in range(n) if degrees[i] == 1]), n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                curr = queue.popleft()
                for neighbor in tree[curr]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)
        
