class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_heap, min_heap = [], []
        max_len, left = 0, 0

        for right in range(len(nums)):
            heappush(min_heap, (nums[right], right))
            heappush(max_heap, (-nums[right], right))

            while min_heap[0][1] < left:
                heappop(min_heap)
            while max_heap[0][1] < left:
                heappop(max_heap)

            if (-max_heap[0][0] - min_heap[0][0]) <= limit:
                max_len = max(max_len, right - left + 1)
            else:
                left += 1
                
        return max_len

        