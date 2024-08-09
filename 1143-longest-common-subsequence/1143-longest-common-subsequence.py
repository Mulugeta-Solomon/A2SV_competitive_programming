class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dp(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0

            if memo[index1][index2] != -1:
                return memo[index1][index2]
            
            if text1[index1] == text2[index2]:
                memo[index1][index2] = dp(index1 + 1, index2 + 1) + 1
            else:
                memo[index1][index2] = max(dp(index1, index2 + 1), dp(index1 + 1, index2))

            return memo[index1][index2]
        

        memo = [[-1] * (len(text2)) for _ in range(len(text1))]
        
        return dp(0, 0)
