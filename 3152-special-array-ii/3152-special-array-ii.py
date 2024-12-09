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
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        union_find, previous = UnionFind(len(nums)), 0
        parity = 'E' if nums[0] % 2 == 0 else 'O'
        
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if previous != i:
                    union_find.union(previous, i)
                continue

            if (nums[i + 1] % 2 == 0 and parity == 'E') or (nums[i + 1] % 2 != 0 and parity == 'O'):
                union_find.union(previous, i)
                previous = i + 1
                parity = 'E' if nums[i + 1] % 2 == 0 else 'O'
                continue

            parity = 'E' if parity == 'O' else 'O'


        result = [False] * len(queries)
        
        for i, (left, right) in enumerate(queries):
            left = union_find.find(left)
            right = union_find.find(right)
            
            if left == right:
                result[i] = True   
            
        return result
