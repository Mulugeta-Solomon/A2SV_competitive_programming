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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols, directions = len(grid), len(grid[0]), [(0, 1), (1, 0), (-1, 0), (0, -1)]
        tree = UnionFind(rows * cols + 1)
        island, result = False, 0

        def inBound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def getIdx(x, y):
            return (x * cols) + y


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    island = True
                    for dr, dc in directions:
                        newRow, newCol = r + dr, c + dc
                        if inBound(newRow, newCol) and grid[newRow][newCol]:
                            tree.union(getIdx(r, c), getIdx(newRow, newCol))


        if not island:
            return result

        for i in range(rows * cols + 1):
            result = max(result, tree.size[i])
        
        return result



        