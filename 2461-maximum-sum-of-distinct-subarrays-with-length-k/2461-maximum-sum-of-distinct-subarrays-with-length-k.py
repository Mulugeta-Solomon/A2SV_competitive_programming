class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left, right, result, curr_wind, lookUp = 0, 0, 0, 0, {}

        while right < len(nums):
            curr = nums[right]
            last_occ = lookUp.get(curr, -1)

            while left <= last_occ or right - left + 1 > k:
                curr_wind -= nums[left]
                left += 1

            lookUp[curr] = right
            curr_wind += nums[right]

            if right - left + 1 == k:
                result = max(result, curr_wind)
            
            right += 1
            
        return result