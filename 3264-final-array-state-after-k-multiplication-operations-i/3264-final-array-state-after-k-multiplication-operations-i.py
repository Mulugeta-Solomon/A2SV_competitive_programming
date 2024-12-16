class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap, count = [], 0
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))
        
        while count < k:
            curr, idx = heappop(heap)
            nums[idx] = curr * multiplier
            heappush(heap, (nums[idx], idx))
            count += 1

        return nums
