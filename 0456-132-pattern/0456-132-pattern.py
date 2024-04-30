class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False 

        stack = deque()
        max_element = float('-inf') # max element so far 

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max_element:
                return True      # Found a valid "132" pattern
            
            while stack and stack[0] < nums[i]:
                max_element = stack.popleft() # update max whenever we found one
            
            stack.appendleft(nums[i]) 

        return False