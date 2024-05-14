class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if mid == 0:
                left = mid + 1
                continue
            if mid == len(arr) - 1:
                right = mid - 1
                continue
                
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            
            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        