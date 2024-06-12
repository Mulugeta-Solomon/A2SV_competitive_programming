class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(start, path):
            if start > len(nums):
                return 
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result 


        