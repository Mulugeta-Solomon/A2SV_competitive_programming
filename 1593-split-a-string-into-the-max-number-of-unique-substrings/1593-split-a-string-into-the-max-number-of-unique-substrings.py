class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        visited = set()
        result = []

        def backtrack(start):
            if start == len(s):
                return 0
            
            result = 0

            for end in range(start + 1, len(s) + 1):
                curr = s[start:end]
                if curr not in visited:
                    visited.add(curr)
                    curr_max = 1 + backtrack(end)
                    result = max(result, curr_max)
                    visited.remove(curr)

            return result

        return backtrack(0) 
                
        