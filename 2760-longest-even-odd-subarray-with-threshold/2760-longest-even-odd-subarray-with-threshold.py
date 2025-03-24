class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        r, curr, result = 0, 0, 0

        while r < len(nums):
            if nums[r] > threshold:
                curr = 0
                r += 1
                continue

            if nums[r] % 2 != curr % 2:
                curr = 0
            
            if nums[r] % 2 == curr % 2:
                curr += 1
                result = max(result, curr)

            r += 1
        
        return result

            
