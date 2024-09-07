class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        freq = Counter(arr1)
        result = []

        for num in arr2:
            while freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        
        for num in sorted(arr1):
            while freq[num] > 0:
                result.append(num)
                freq[num] -= 1
            
        return result 