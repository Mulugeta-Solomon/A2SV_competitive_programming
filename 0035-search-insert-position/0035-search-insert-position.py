class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                if nums[mid - 1] < target:
                    return mid 
                right = mid - 1

            elif nums[mid] < target:
                if nums[mid + 1] > target:
                    return mid + 1
                left = mid + 1

            else:
                return mid 
        
        