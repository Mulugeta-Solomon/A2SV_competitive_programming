class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [nums1[i] - nums2[i] for i in range(len(nums1))]
        self.count = 0

        def merge(left: List[int], right: List[int]):
            i, j = 0, 0 # get the pairs 
            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    self.count += len(right) - j
                    i += 1
                else:
                    j += 1
            
            l, r, k = 0, 0, 0 # merge the arr 
            result  = [0] * (len(left) + len(right))

            while l < len(left) and r < len(right):
                if left[l] > right[r]:
                    result[k] = right[r]
                    r += 1
                    k += 1
                
                else:
                    result[k] = left[l]
                    l += 1
                    k += 1
                
            while l < len(left):
                result[k] = left[l]
                l += 1
                k += 1
            
            while r < len(right):
                result[k] = right[r]
                r += 1
                k += 1
            
            return result

        def mergeSort(left: int, right: int, arr):
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left) // 2

            left_arr = mergeSort(left, mid, arr)
            right_arr = mergeSort(mid + 1, right, arr)

            return merge(left_arr, right_arr)
        
        mergeSort(0, len(nums) - 1, nums)

        return self.count