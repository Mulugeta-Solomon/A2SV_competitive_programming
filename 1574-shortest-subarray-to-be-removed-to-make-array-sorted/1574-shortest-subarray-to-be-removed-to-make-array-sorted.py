class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        result = right

        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            
            result = min(result, right - left - 1)
            left += 1
            
        return result 