class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        left, right = 0, len(nums) - 1
        result = []

        def binarySearch(left, right):
            if left > right:
                return []
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return [mid] + binarySearch(left, mid - 1) + binarySearch(mid + 1, right)
            if nums[mid] < target:
                return binarySearch(mid + 1, right)
            else:
                return binarySearch(left, mid - 1)

        result = binarySearch(left, right)
        result.sort()
        return result             
