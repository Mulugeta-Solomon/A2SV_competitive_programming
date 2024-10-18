class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr |= num
        
        def backtrack(idx, curr):
            if idx == len(nums):
                if curr == maxOr:
                    return 1
                return 0
            
            incl = backtrack(idx + 1, curr | nums[idx]) # include the curr element 
            excl = backtrack(idx + 1, curr) # exclude the curr element 

            return incl + excl

        return backtrack(0, 0)