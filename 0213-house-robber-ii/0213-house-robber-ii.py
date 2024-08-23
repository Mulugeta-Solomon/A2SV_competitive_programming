class Solution:
    def dp(self, mem, nums, i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        if i not in mem:
            mem[i] = max(self.dp(mem,nums, i - 1), nums[i] + self.dp(mem,nums, i - 2))
        
        return mem[i]

    def rob(self, nums):
        n = len(nums)

        if n <= 2:
            return max(nums)
            
        case1 = nums[:-1]
        case2 = nums[1:]
        
        return max(self.dp(dict(),case1, n - 2), self.dp(dict(),case2, n - 2))