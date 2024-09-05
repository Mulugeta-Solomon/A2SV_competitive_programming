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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = UnionFind(n + 1)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph.union(i + 1, j + 1)
        
        repre = set()
        for i in range(1, n + 1):
            repre.add(graph.find(i))
        
        return len(repre)
        
        