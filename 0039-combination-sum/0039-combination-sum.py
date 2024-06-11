class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path):
            if target == sum(path):
                result.append(path[:])
                return 
            if target < sum(path):
                return 

            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]])
        
        backtrack(0, [])
        
        return result 
