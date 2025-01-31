class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x): # Iterative way of path compression 
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        union_find = UnionFind(row * col)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def flatten(x, y):
            return x * col + y
        
        def inbound(x, y):
            return 0 <= x < row and 0 <= y < col
        zero = False
        for r in range(row):
            for c in range(col):
                if not grid[r][c]:
                    zero = True
                    continue
                curr = flatten(r, c)
                for dr, dc in directions: # Find neighbour
                    nr, nc = r + dr, c + dc
                    if inbound(nr, nc) and grid[nr][nc]:
                        neighbor = flatten(nr, nc)
                        union_find.union(curr, neighbor)
        if not zero:
            return row * col
        

        result = 0  # max_island_size

        for r in range(row):
            visited = set()
            for c in range(col):
                if not grid[r][c]:
                    curr = 1 # start with the flipped '0'

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if inbound(nr, nc) and grid[nr][nc]:
                            neighbor = flatten(nr, nc)

                            neigh_root = union_find.find(neighbor)
                            if neigh_root not in visited:
                                curr += union_find.size[neigh_root]
                            visited.add(neigh_root)
                    
                    result = max(result, curr)
        
        return result 
                    