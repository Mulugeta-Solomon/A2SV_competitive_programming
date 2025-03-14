class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i]:
                for j in range(i + 1, len(nums) - 1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        result += (k - j)
                        k += 1
        
        return result 