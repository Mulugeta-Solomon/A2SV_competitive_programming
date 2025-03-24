class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, result = 0, 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 1  and left < right:
                left += 1
            
            if nums[right] - nums[left] == 1:
                result = max(result, right - left + 1)
        
        return result
        