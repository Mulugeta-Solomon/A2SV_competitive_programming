class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        result = 0

        while k > 0:
            curr = -heappop(heap)

            result += curr
            heappush(heap, -math.ceil(curr/3))

            k -= 1
        
        return result

        