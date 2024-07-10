class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for src in range(len(bombs)):
            for dst in range(src + 1, len(bombs)):
                x1, y1, r1 = bombs[src]
                x2, y2, r2 = bombs[dst]

                distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

                if r1 >= distance:
                    graph[src].append(dst)
                if r2 >= distance:
                    graph[dst].append(src)
        
        def bfs(node):
            queue = deque([node])
            visited = set()
            visited.add(node)

            while queue:
                size = len(queue)
                for _ in range(size):
                    src = queue.popleft()

                    for dst in graph[src]:
                        if dst not in visited:
                            queue.append(dst)
                            visited.add(dst)
            return len(visited)
        
        max_bombs = 0
        for i in range(len(bombs)):
            max_bombs = max(max_bombs, bfs(i))

            if max_bombs == len(bombs):
                return max_bombs
        
        return max_bombs

