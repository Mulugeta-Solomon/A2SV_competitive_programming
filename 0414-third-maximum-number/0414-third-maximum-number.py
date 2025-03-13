class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in set(nums):
            if num >= first:
                third = second
                second = first 
                first = num
                continue
        
            if num >= second:
                third = second
                second = num
                continue
            
            if num >= third:
                third = num
        
        return third