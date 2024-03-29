class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod, zero_count, idx = 1,nums.count(0), None
        if zero_count > 1:
            return [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
    

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = prod
            else:
                nums[i] = int((prod / nums[i]) *  (0 if zero_count == 1 else 1))
        
        return nums

        
        