class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def merge(arr1, arr2) -> List[int]:
            merged = [0] * (len(arr1) + len(arr2))
            i, j, k = 0, 0, 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged[k] = arr1[i]
                    i += 1
                    k += 1
                    continue
                merged[k] = arr2[j]
                j += 1
                k += 1
            
            while i < len(arr1):
                merged[k] = arr1[i]
                i += 1
                k += 1

            while j < len(arr2):
                merged[k] = arr2[j]
                j += 1
                k += 1

            return merged 

        merged = merge(nums1, nums2)
        idx = len(merged) // 2
        
        if len(merged) % 2 == 0:
            return (merged[idx] + merged[idx-1]) / 2

        return merged[idx]
        
        