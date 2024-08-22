class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        memo = [[0] * cols for _ in range(rows)]

        memo[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for row in range(rows - 2, -1, -1):
            memo[row][-1] = max(1, memo[row + 1][-1] - dungeon[row][-1])
        
        for col in range(cols - 2, -1, -1):
            memo[-1][col] = max(1, memo[-1][col + 1] - dungeon[-1][col])

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                memo[row][col] = max(1, min(memo[row][col + 1], memo[row + 1][col]) - dungeon[row][col]) 

        return memo[0][0]
