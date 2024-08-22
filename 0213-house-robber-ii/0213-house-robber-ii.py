class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1: return nums[0]

        memo1 = [0] * (n)
        memo1[0] = nums[0]
        memo1[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            memo1[i] = max(memo1[i - 1], memo1[i - 2] + nums[i])

        memo2 = [0] * (n)
        memo2[-1] = nums[-1]
        memo2[-2] = max(nums[-1], nums[-2])

        for i in range(n - 3, 0, -1):
            memo2[i] = max(memo2[i + 1], memo2[i + 2] + nums[i])
    

        return max(memo1[-2], memo2[1])