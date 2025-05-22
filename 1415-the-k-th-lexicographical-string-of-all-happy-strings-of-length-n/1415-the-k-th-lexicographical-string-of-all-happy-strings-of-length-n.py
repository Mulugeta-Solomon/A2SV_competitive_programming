class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(curr, i):
            if len(curr) == n:
                result.append(curr[:])
                return 

            for j in range(3):
                if i != j:
                    curr.append(chars[j])
                    backtrack(curr, j)
                    curr.pop()

        result = []
        chars = ['a', 'b', 'c']
        for i in range(3):
            curr = [chars[i]]
            backtrack(curr, i)
        
        
        return '' if len(result) < k else ''.join(result[k - 1])
