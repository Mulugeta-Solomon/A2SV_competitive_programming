class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i] 

        right_most_sum = prefix_sum[len(prefix_sum) - 1]

        for i in range(1,len(prefix_sum)):
            if right_most_sum - prefix_sum[i] == prefix_sum[i - 1]:
                return i-1

        return -1
