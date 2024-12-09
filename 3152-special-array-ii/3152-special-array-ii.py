class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        subarr, previous = [], 0
        parity = 'E' if nums[0] % 2 == 0 else 'O'
        
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if previous != i:
                    subarr.append([previous, i])
                continue

            if (nums[i + 1] % 2 == 0 and parity == 'E') or (nums[i + 1] % 2 != 0 and parity == 'O'):
                subarr.append([previous, i])
                previous = i + 1
                parity = 'E' if nums[i + 1] % 2 == 0 else 'O'
                continue

            parity = 'E' if parity == 'O' else 'O'

        def binarysearch(arr, target):
            left, right = 0, len(arr) - 1
      
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid][0] <= target <= arr[mid][1]:
                    return mid

                if arr[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1  

        result = [False] * len(queries)
        
        for i, (left, right) in enumerate(queries):
            left = binarysearch(subarr, left)
            right = binarysearch(subarr, right)
            
            if left == right:
                result[i] = True   
            
        return result
