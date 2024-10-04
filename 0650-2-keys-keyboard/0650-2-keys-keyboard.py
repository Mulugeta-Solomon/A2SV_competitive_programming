class Solution:
    def minSteps(self, n: int) -> int:
        
        opr, prev, copy = 0, 1, 0

        while True:
            if 2 * prev > n: # paste operation
                if prev >= n:
                    return opr
                prev += copy
                opr += 1

            elif 2 * prev <= n: # copy and paste operation
                copy = prev
                prev += copy
                opr += 2
            else:
                return opr

                

