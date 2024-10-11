class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        nums = [(nums[i], i) for i in range(len(nums))]
        
        def merge(left, right):
            temp = [0] * (len(left) + len(right))
            i, j, k = 0, 0, 0
            
            prefix = 0 
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    temp[k] = (right[j][0], right[j][1])
                    prefix += 1
                    j += 1
                else:
                    temp[k] = (left[i][0], left[i][1])
                    result[left[i][1]] += prefix
                    i += 1
                k += 1
            
            while i < len(left):
                temp[k] = (left[i][0], left[i][1])
                result[left[i][1]] += prefix
                k += 1
                i += 1

            while j < len(right):
                temp[k] = (right[j][0], right[j][1])
                k += 1
                j += 1
            
            
            return temp
            
        def mergeSort(left, right):
            if left == right:
                return [(nums[left][0], nums[left][1])]
            
            mid = left + (right - left)//2

            left_half = mergeSort(left , mid)
            right_half = mergeSort(mid + 1, right)

            return merge(left_half, right_half)
        
        mergeSort(0, len(nums) - 1)
        
        return result
        