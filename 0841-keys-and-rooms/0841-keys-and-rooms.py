class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        queue = deque([(0)])

        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()
                visited.add(curr)
                for key in rooms[curr]:
                    if key not in visited:
                        queue.append(key)
        
        return len(visited) == len(rooms)