class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        min_operation, prev = 0, nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > prev:
                temp = ceil(nums[i] / prev)
                prev = nums[i] // temp
                min_operation += temp - 1

            else:
                prev = nums[i]
        
        return min_operation

