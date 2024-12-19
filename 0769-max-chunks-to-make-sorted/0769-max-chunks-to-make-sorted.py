class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        stack = []

        for i in range(len(arr)):
            if not stack or arr[i] > arr[stack[-1]]:
                stack.append(i)
            else:
                MAX = stack[-1]
                while stack and arr[i] < arr[stack[-1]]:
                    stack.pop()
                stack.append(MAX)
        
        return len(stack)