class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        freq, result = {}, 0

        for num in nums1:
            freq[num] = freq.get(num, 0) + n2
        for num in nums2:
            freq[num] = freq.get(num, 0) + n1
        
        for num in freq:
            if freq[num] % 2:
                result = result ^ num
        
        return result 
