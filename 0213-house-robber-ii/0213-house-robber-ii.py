class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) <= 2:
            return max(nums)
        

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = nums[0]
        t2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = t2
            t2 = max(nums[i] + t1, t2)
            t1 = temp

        return t2