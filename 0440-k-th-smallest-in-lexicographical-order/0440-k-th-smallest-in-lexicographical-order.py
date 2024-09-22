class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        curr, i = 1, 1

        def count(curr):
            result = 0
            neighbor = curr + 1

            while curr <= n:
                result += min(neighbor, n + 1) - curr
                curr *= 10
                neighbor *= 10
            
            return result

        while i < k:
            steps = count(curr)

            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1
        
        return curr

