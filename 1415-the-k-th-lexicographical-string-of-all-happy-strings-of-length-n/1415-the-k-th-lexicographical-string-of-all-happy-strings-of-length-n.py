class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(curr, i):
            if len(curr) == n:
                result.append(curr[:])
                return 
            
            for j in range(3):
                if i != j:
                    curr.append(choices[j])
                    backtrack(curr, j)
                    curr.pop()


        choices, result = ['a', 'b', 'c'], []
        for i in range(3):
            curr = [choices[i]]
            backtrack(curr, i)
        

        if len(result) < k:
            return ''
        return ''.join(result[k - 1])
