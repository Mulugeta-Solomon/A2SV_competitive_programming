class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        curr, heap, result, MOD = 0, [], float('-inf'), 10 ** 9 + 7

        for eff, spd in sorted(zip(efficiency, speed), reverse=True):
            while len(heap) > k - 1:
                curr -= heappop(heap)

            heappush(heap, spd)
            curr += spd 
            result = max(result, curr * eff)
        
        return result % MOD