class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i].append((i, j))
                    cols[j].append((i, j))
        
        visited = set()
        for row, servers in rows.items():
            if len(servers) >= 2:
                for (i, j) in servers:
                    if (i, j) not in visited:
                        visited.add((i, j))
        
        for col, servers in cols.items():
            if len(servers) >= 2:
                for (i, j) in servers:
                    if (i, j) not in visited:
                        visited.add((i, j))
        
        return len(visited)
                
