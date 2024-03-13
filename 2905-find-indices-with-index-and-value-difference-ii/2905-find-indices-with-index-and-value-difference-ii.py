class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        prev_max, prev_min, max_idx, min_idx = -float('inf'), float('inf'), -1, -1

        for right in range(indexDifference, len(nums)):
            left = right - indexDifference 

            if nums[left] > prev_max:
                prev_max = nums[left]
                max_idx = left
            if nums[left] < prev_min:
                prev_min = nums[left]
                min_idx = left
            
            if abs(prev_max - nums[right]) >= valueDifference:
                return [max_idx, right]
            if abs(prev_min - nums[right]) >= valueDifference:
                return [min_idx, right]
        
        return [-1, -1]
