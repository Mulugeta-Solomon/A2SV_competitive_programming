from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_queue = deque()
        min_queue = deque()
        result, left = 0, 0

        for i in range(len(nums)):
            while max_queue and nums[i] > nums[max_queue[-1]]:
                max_queue.pop()
            
            max_queue.append(i)

            while min_queue and nums[i] < nums[min_queue[-1]]:
                min_queue.pop()
            
            min_queue.append(i)

            while nums[max_queue[0]] - nums[min_queue[0]] > 2:
                if min_queue[0] > max_queue[0]:
                    left = max_queue[0] + 1
                    max_queue.popleft()
                else:
                    left = min_queue[0] + 1
                    min_queue.popleft()

            result += i - left + 1
        
        return result 