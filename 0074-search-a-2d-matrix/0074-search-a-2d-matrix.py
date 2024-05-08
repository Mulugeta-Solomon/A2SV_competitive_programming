class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        
        for i in range(row):  
           result = self.binarySearch(matrix[i][:], target)
           if result == True:
            return True
        
        return False 

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True 
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False 

        