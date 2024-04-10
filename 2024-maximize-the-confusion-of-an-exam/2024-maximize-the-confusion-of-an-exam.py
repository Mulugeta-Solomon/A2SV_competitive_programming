class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        true_max = self.solve(answerKey, k, 'T')
        false_max = self.solve(answerKey, k, 'F')
        
        return max(true_max, false_max)
        
    def solve(self, answerKey: str, k: int, option: str) -> int:

        max_count, left, used = float('-inf'), 0, 0
        
        for right in range(len(answerKey)):
            if answerKey[right] != option:
                used += 1

            while used > k:
                if answerKey[left] != option:
                    used -= 1
                left += 1

        max_count = max(max_count, right - left + 1)
        
        return max_count