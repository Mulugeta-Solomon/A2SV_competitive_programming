class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left, right = 0, len(nums) - 1

        starting_pos = self.startingPosition(nums, left, right, target) 
        ending_pos = self.endingPosition(nums, left, right, target)

        return [starting_pos, ending_pos]
    
    def startingPosition(self, nums: List[int], left: int, right: int, target: int) -> int:

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid == 0 or nums[mid-1] != nums[mid]:
                    return mid 
                else:
                    right = mid - 1
        
        return -1

    
    def endingPosition(self, nums: List[int], left: int, right: int, target: int) -> int:
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != nums[mid]:
                    return mid 
                else:
                    left = mid + 1
        
        return -1

        