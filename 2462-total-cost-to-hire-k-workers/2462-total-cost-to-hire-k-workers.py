class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        heapLeft, heapRight, inf = [], [], float('inf')
        left, right, result = 0, len(costs) - 1, 0

        while k > 0:
            while len(heapLeft) < candidates and left <= right:
                heappush(heapLeft, costs[left])
                left += 1
            
            while len(heapRight) < candidates and left <= right:
                heappush(heapRight, costs[right])
                right -= 1
            
            cand1 = heapLeft[0] if heapLeft else inf
            cand2 = heapRight[0] if heapRight else inf
            
            # Compare the two candidtes (i.e. left is always with smaller index)
            if cand1 <= cand2:
                result += heappop(heapLeft)
            else:
                result += heappop(heapRight)

            k -= 1

        return result 


        
        return sum(hired)