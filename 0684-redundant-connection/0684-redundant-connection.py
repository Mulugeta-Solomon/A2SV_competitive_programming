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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0

        for u, v in edges:
            n = max(n, u, v)
        
        graph = UnionFind(n + 1)
        i, idx = 0, None
        while i < len(edges):
            u, v = edges[i]
            if graph.find(u) != graph.find(v):
                graph.union(u, v)
            else:
                idx = i

            i += 1

        return edges[idx] 

        