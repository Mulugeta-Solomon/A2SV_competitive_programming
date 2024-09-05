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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
            
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        distance = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heappush(distance, (manhattan(points[i], points[j]), i, j))
 
        graph, edgesVisited = UnionFind(len(points)), 0
        result = 0
        while edgesVisited < len(points) - 1:
            dist, u, v = heappop(distance) 

            if graph.find(u) != graph.find(v):
                result += dist
                graph.union(u, v)
                edgesVisited += 1

        
        return result
            



