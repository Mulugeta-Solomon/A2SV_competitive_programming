class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = nums[0]

        for num in nums[1:]:
            result ^= num
        
        return result
