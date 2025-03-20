class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        curr, left, max_len = 0, 0, 0

        for right in range(len(nums)):
            while curr & nums[right] != 0: # conflic exist
                curr ^= nums[left] # remove leftmost element
                left += 1
            curr |= nums[right]
            max_len = max(max_len, right - left + 1)
        
        return max_len
