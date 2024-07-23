class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        min_patches = 0
        curr = 1

        i = 0
        
        while curr <= n:
            if i < len(nums) and nums[i] <= curr:
                curr += nums[i]
                i += 1
            else:
                curr *= 2
                min_patches += 1
        
        return min_patches 