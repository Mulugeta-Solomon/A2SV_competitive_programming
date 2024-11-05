class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    # def find(self, x):
    #     if x == self.root[x]:
    #         return x
    #     self.root[x] = self.find(self.root[x])
    #     return self.root[x]

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

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        graph = UnionFind(n * n * 4)

        for row in range(n):
            for col in range(n):
                currIdx = 4 * (row * n + col)
                if grid[row][col] == ' ':
                    graph.union(currIdx, currIdx + 1) 
                    graph.union(currIdx + 1, currIdx + 2)
                    graph.union(currIdx + 2, currIdx + 3)
                
                if grid[row][col] == '/':
                    graph.union(currIdx, currIdx + 3)
                    graph.union(currIdx + 1, currIdx + 2)
                
                if grid[row][col] == '\\':
                    graph.union(currIdx, currIdx + 1)
                    graph.union(currIdx + 2, currIdx + 3)
                
                if col < n - 1:
                    graph.union(currIdx + 1, (currIdx + 4) + 3) # union with the right cell
                
                if row < n - 1:
                    graph.union(currIdx + 2, (currIdx + 4 * n)) # union with the cell bellow 
        
        result = 0
        for i in range(n * n * 4):
            if graph.find(i) == i:
                result += 1
        
        return result


                
                
        