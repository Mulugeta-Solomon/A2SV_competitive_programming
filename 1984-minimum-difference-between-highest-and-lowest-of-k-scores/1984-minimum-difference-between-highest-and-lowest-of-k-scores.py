class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, result = 0, k - 1, float('inf')

        while r < len(nums):
            result = min(result, nums[r] - nums[l])
            r += 1
            l += 1
        
        return result