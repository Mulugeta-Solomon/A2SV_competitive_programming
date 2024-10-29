class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            return -1
        
        queue, prefix_sum = deque(), [0] * (len(nums) + 1)

        for i in range (len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        result = float('inf')
        for idx, val in enumerate(prefix_sum):

            while queue and val <= prefix_sum[queue[-1]]:
                queue.pop()
            
            while queue and val - prefix_sum[queue[0]] >= k:
                result = min(result, idx - queue.popleft())

            queue.append(idx)
        
        return result if result != float('inf') else -1