class Solution:
    def maxScore(self, s: str) -> int:
        
        suffix_sum_ones, prefix_sum_zeros, max_score = [0] * len(s), 0, float('-inf')
        suffix_sum_ones[len(s) - 1] = int(s[len(s) - 1])
        
        for i in range(len(s) - 2, -1, -1):
            suffix_sum_ones[i] = suffix_sum_ones[i+1] + int(s[i])

        for i in range(len(s)-1):
            if s[i] == '0':
                prefix_sum_zeros += 1

            max_score = max(max_score, prefix_sum_zeros + suffix_sum_ones[i+1])

        return max_score 