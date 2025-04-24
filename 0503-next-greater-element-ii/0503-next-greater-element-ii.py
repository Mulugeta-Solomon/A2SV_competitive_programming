class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lookup, stack, n = defaultdict(lambda:-1), [], len(nums)

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                lookup[stack[-1]] = nums[i % n] 
                stack.pop()
            stack.append(i % n)

        return [lookup[i] for i in range(n)]