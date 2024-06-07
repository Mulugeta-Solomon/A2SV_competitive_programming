class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(curr):
            if len(curr) == n:
                result.append(curr[:])
                return 
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
        
        backtrack([])
        return result 
                
                



        