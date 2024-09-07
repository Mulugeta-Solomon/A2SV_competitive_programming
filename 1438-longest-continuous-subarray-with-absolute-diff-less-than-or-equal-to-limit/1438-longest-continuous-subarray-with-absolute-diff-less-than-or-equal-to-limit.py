class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_queue, min_queue = deque(), deque()
        max_len, left = 0, 0

        for right in range(len(nums)):
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[right])
            
            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > limit: # check the current window is valid
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                left += 1
            
            max_len = max(max_len, right - left + 1)

            
        return max_len

        