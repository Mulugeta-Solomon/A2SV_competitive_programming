class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for row in matrix:
            if binary_search(row):
                return True
        
        return False