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
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = UnionFind(26)

        for equation in equations:
            if equation[1] == '=':
                graph.union(ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a'))
        
        for equation in equations:
            if equation[1] == '!':
                if graph.find(ord(equation[0]) - ord('a')) == graph.find(ord(equation[3]) - ord('a')):
                    return False
        
        return True


