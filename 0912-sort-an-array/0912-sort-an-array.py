class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left: List[int], right: List[int]) -> List[int]: 
            n, m = len(left), len(right)
            temp = [0] * (n + m)
            i, j, k = 0, 0, 0

            while i < n and j < m:
                if left[i] > right[j]:
                    temp[k] = right[j]
                    j += 1
                else:
                    temp[k] = left[i]
                    i += 1
                k += 1

            while i < n:
                temp[k] = left[i]
                i += 1
                k += 1

            while j < m:
                temp[k] = right[j] 
                j += 1
                k += 1
            
            return temp
        
        def mergeSort(left: int, right: int):
            if left == right:
                return [nums[left]]
            
            mid = left  + (right - left) // 2
            
            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)

            return merge(left_half, right_half)
        
        return mergeSort(0, len(nums) - 1)

        