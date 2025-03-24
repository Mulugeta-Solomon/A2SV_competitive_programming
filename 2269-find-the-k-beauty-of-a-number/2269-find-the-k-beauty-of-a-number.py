class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """

        l, r, result = 0, k - 1, 0
        nums = str(num)

        while r < len(nums):
            curr = int(nums[l:r + 1])
            if curr > 0 and num % curr == 0:
                result += 1
            r += 1
            l += 1

        return result
        
        