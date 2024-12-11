class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, result = 0, 0, 0

        while right < len(nums):
            
            while nums[right] - nums[left] > 2 * k:
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result