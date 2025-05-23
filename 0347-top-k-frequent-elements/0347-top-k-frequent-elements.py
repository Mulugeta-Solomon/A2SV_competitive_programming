class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap, result = [], []

        for num, v in count.items():
            heappush(max_heap, (-v, num))
        
        while k > 0:
            _, num = heappop(max_heap)
            result.append(num)
            k -= 1

        return result
