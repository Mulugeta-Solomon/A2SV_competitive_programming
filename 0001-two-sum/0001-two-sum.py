class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookUp = {}

        for idx, value in enumerate(nums):
            diff = target - value

            if diff in lookUp:
                return [lookUp[diff], idx]

            lookUp[value] = idx
                
        
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''  