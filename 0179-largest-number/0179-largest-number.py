class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
                
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        nums = sorted(nums, key = cmp_to_key(compare))
        
        return ''.join(nums) if nums[0] != '0' else '0'
        