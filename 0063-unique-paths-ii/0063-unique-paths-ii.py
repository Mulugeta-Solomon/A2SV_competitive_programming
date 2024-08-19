class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        row, col = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * col for _ in range(row)]

        if obstacleGrid[0][0] == 0:
            memo[0][0] = 1
        else:
            memo[0][0] = 0

        for i in range(1, row):
             if obstacleGrid[i][0] == 0:
                memo[i][0] = memo[i-1][0]
            
        for i in range(1, col):
            if obstacleGrid[0][i] == 0:
                memo[0][i] = memo[0][i-1]
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]

        return memo[-1][-1]
