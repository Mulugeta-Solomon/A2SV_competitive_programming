class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        if len(cardPoints) == k:
            return sum(cardPoints)

        n = len(cardPoints)
        prefix_sum, total, max_score = sum(cardPoints[:n-k]), sum(cardPoints), 0
        left, right = 0, n-k
        print(prefix_sum, total)
        while right < n:
            max_score = max(max_score, total - prefix_sum)
            prefix_sum += cardPoints[right] - cardPoints[left]
            right += 1
            left += 1
        
        max_score = max(max_score, total - prefix_sum)
        
        return max_score