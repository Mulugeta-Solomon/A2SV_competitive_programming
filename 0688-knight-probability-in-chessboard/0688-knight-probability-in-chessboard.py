class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        memo = [[0] * n for _ in range(n)]
        memo[row][column] = 1

        def isInbound(x, y):
            return 0 <= x < n and 0 <= y < n

        for _ in range(k):

            curr = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if memo[i][j] == 0:
                        continue 
                    
                    for row, col in directions:
                        newRow, newCol = i + row, j + col

                        if isInbound(newRow, newCol):
                            curr[newRow][newCol] += memo[i][j] / 8
            
            memo = curr
        
        return sum([sum(row) for row in memo])
        