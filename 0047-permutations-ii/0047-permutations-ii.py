class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) == len(nums):
                if tuple(curr) not in perm:
                    result.append(curr[:])
                    perm.add(tuple(curr[:]))
                return 
            
            for j in range(len(nums)):
                if j not in visited:
                    visited.add(j)
                    curr.append(nums[j])
                    backtrack(curr, j)
                    visited.remove(j)
                    curr.pop()

        
        visited, perm, result  = set(), set(), []
        for i in range(len(nums)):
            curr = [nums[i]]
            visited.add(i) 
            backtrack(curr, i)
            visited = set()
        
        return result
        