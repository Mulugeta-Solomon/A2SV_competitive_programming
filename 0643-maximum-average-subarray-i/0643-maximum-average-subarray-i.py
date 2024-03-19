class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if k == len(nums):
            return sum(nums)/k

        left, right, max_average = 0, k, float('-inf')
        curr_sum = sum(nums[:k])
    
        while right <= len(nums):
            curr_window_average = curr_sum / k
            max_average = max(max_average, curr_window_average)
            
            if right == len(nums):
                break 
            curr_sum += (nums[right] - nums[left])
            right += 1
            left += 1

    
        return max_average 
        