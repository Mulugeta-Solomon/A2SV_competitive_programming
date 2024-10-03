class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        
        prefixSum, lookUp, minLength = 0, {0 : -1}, len(nums)

        for i, num in enumerate(nums):
            prefixSum += num
            currMOD = prefixSum % p
            target = (currMOD - remainder + p) % p 

            if target in lookUp:
                minLength = min(minLength, i - lookUp[target])
            
            lookUp[currMOD] = i
        
        return minLength if minLength < len(nums) else -1
