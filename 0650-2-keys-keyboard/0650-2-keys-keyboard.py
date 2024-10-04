class Solution:
    @cache
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        def dfs(copy, paste):
            if copy == n:
                return 0
            if copy > n:
                return float('inf')
            
            opr1 = 2 + dfs(copy * 2, copy) # copy and paste
            opr2 = 1 + dfs(copy + paste, paste) # paste
            
            return min(opr1, opr2)
        
        return 1 + dfs(1, 1)



        
        # opr, prev, copy = 0, 1, 0

        # while True:
        #     if 2 * prev > n: # paste operation
        #         if prev >= n:
        #             return opr
        #         prev += copy
        #         opr += 1

        #     elif 2 * prev <= n: # copy and paste operation
        #         copy = prev
        #         prev += copy
        #         opr += 2


                

