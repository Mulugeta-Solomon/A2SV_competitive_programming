class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = self.firstOccurence(nums,len(nums),target)

        end_index = self.lastOccurence(nums, 0, len(nums) - 1,target, len(nums))
        return [start_index, end_index]


    def firstOccurence(self,arr, n, x): 
        start = 0 
        end = n-1

        while(start <= end):
            mid=(start + end) // 2
            if(arr[mid] < x):
                start = mid + 1 
            elif(arr[mid] > x):
                end = mid-1 
            else:
                if mid == 0 or arr[mid-1] != arr[mid]:
                    return mid 
                else:
                    end = mid - 1
        
        return -1
    
    def lastOccurence(self, arr, low, high, x, n):
        if (high >= low):
            mid = low + (high - low) // 2
            if ((mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x):
                return mid
            elif (x < arr[mid]):
                return self.lastOccurence(arr, low, (mid - 1), x, n)
            else:
                return self.lastOccurence(arr, (mid + 1), high, x, n)
    
        return -1
        
        

