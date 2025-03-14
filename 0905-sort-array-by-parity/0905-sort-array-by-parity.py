class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p, s = 0, 0
        
        while s < len(nums):
            if not nums[s] % 2:
                nums[s], nums[p] = nums[p], nums[s]
                p += 1
            s += 1

        return nums