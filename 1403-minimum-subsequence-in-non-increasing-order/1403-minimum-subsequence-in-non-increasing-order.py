class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result, maxx, curr = [], sum(nums), 0
        for num in nums[::-1]:
            curr += num
            if curr > maxx - curr:
                result.append(num)
                return result
            result.append(num)
        
        return result
         