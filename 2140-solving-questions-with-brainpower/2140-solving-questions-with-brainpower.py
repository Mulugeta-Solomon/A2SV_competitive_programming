class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        memo = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            point, brainpower = questions[i]

            next = min(n, i + brainpower + 1)
            memo[i] = max(memo[i+1], point + memo[next]) # if memo[i+1] is large skip current 
        
        return memo[0]