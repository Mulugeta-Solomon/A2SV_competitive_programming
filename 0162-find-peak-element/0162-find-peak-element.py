class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums = [float('-inf')] + nums + [float('-inf')]
        print(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2 

            if mid == 0:
                left = mid + 1
                continue
            if mid == len(nums) - 1:
                right = mid - 1
                continue 
            
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid - 1
            
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        