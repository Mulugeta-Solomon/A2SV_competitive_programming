class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = 0
        count = set(nums)
        s = nums[0]
        for i in nums:
            count1 = 1
            while i * i < 100000:
                if i * i in count:
                    count1 += 1
                else:
                    break
                i = i * i
            res = max(count1,res)
        if res > 2:
            return res
        else:
            return -1
        