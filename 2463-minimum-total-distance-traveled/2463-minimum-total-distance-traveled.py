class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factory.sort()
        fact_pos = []
        for f in factory:
            for _ in range(f[1]):
                fact_pos.append(f[0])

        robo, fact = len(robot), len(fact_pos)

        dp = [[0] * (fact + 1) for _ in range(robo + 1)]

        for i in range(robo):
            dp[i][-1] = float('inf')
        
        for i in range(robo - 1, -1, -1):
            for j in range(fact - 1, -1, -1):
                noskip = abs(robot[i] - fact_pos[j]) + dp[i + 1][j + 1] # choose curr factory
                skip = dp[i][j + 1] # skip

                dp[i][j] = min(noskip, skip)

        return dp[0][0]


