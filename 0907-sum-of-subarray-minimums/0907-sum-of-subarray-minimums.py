class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10 ** 9 + 7
        stack = []
        result = 0

        for i in range(len(arr)):
            while stack and arr[i] < stack[-1][1]:
                idx, val = stack.pop()
                left = idx - stack[-1][0] if stack else idx + 1
                right = i - idx
                result = (result + val * left * right) % MOD
            stack.append((i, arr[i]))
        
        for i in range(len(stack)):
            idx, val = stack[i]
            left = idx - stack[i-1][0] if i > 0 else idx + 1
            right = len(arr) - idx 
            result = (result + val * left * right ) % MOD
        
        return result

