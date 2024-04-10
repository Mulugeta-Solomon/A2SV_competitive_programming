class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        sum_ = sum(chalk)
        target, prefix_sum = k % sum_, 0

        for right in range(len(chalk)):
            prefix_sum += chalk[right]
            if prefix_sum > target:
                return right