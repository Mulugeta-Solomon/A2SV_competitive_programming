class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)

        for i in range(len(routes)):
            for station in routes[i]:
                graph[station].append(i)

        queue, visited = deque(), set()
        queue.append(source)
        visited.add(source)
        cost = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == target:
                    return cost
                for bus in graph[curr]:
                    for station in routes[bus]:
                        if station not in visited:
                            queue.append(station)
                            visited.add(station)
                    routes[bus] = []
            cost += 1
        
        return -1
