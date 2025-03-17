class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        
    def inbound(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size 
    
    def getIndex(self, target:int):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == target:
                    return r, c 

    def adjacentSum(self, value: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        r, c = self.getIndex(value)
        result = 0

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.inbound(nr, nc):
                print(self.grid[nr][nc])
                result += self.grid[nr][nc]
        
        return result


    def diagonalSum(self, value: int) -> int:
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        r, c = self.getIndex(value)
        result = 0
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.inbound(nr, nc):
                result += self.grid[nr][nc]
        
        return result
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)