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
        visited = set()

        def inBound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def getIdx(x, y):
            return (x * cols) + y

        def dfs(row, col):
            if not grid[row][col] or (row, col) in visited:
                return 
            
            visited.add((row, col))
            idx = getIdx(row, col)

            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if inBound(newRow, newCol):
                    if grid[newRow][newCol] and (newRow, newCol) not in visited:
                        newIdx = getIdx(newRow, newCol)
                        tree.union(idx, newIdx)
                        dfs(newRow, newCol)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    dfs(r, c)
        print(tree.size)
        result = set()
        for i in range(rows * cols + 1):
            result.add(tree.find(i))
        
        return len(result)



        