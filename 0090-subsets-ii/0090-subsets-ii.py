class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        visited = set()
        nums.sort()

        def backtrack(idx, curr):
            if idx == len(nums):
                if curr and tuple(curr[:]) not in visited:
                    result.append(curr[:])
                    visited.add(tuple(curr[:]))
                return 
       
            if curr and tuple(curr[:]) not in visited:
                result.append(curr[:])
                visited.add(tuple(curr[:]))
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                if curr:
                    backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        
        return result