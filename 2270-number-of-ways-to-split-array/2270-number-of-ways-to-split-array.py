class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        suffix_sum, prefix_sum, result = sum(nums), 0, 0

        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            suffix_sum -= nums[i]
            if prefix_sum >= suffix_sum:
                result += 1 

        return result