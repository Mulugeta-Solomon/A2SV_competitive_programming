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
    def removeStones(self, stones: List[List[int]]) -> int:

        unionFind = UnionFind(len(stones) + 1)

        edges = []
        lookUpX, lookUpY = {}, {}

        for i, stone in enumerate(stones):
            x, y = stone

            if x in lookUpX:
                edges.append((i, lookUpX[x]))
            else:
                lookUpX[x] = i
            
            if y in lookUpY:
                edges.append((i, lookUpY[y]))
            else:
                lookUpY[y] = i
        
        result = 0
        for u, v in edges:
            if unionFind.find(u) != unionFind.find(v):
                unionFind.union(u, v)
                result += 1
        
        return result 
        