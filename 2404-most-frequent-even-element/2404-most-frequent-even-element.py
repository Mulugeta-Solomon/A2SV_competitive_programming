class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        lookUp = {}
        for num in nums:
            if num % 2 == 0:
                lookUp[num] = lookUp.get(num, 0) + 1

        if not lookUp:
            return -1
        
        result = [float('inf'), 0]
        for num, freq in lookUp.items():
            if freq > result[1]:
                result = [num, freq]
            
            if freq == result[1]:
                if num < result[0]:
                    result = [num, freq]
        
        return result[0]

