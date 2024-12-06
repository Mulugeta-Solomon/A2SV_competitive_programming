class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned, result, curr, total = set(banned), 0, 1, 0

        while curr <= n:
            if (total + curr) > maxSum:
                return result 
            if curr not in banned:
                total += curr
                result += 1

            curr += 1
               
        return result
            

