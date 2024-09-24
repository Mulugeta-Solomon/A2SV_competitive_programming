class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack, count = [], 1

        for char in s:
            if stack and stack[-1][0] == char:
                count = stack[-1][1] + 1
                stack.append((char, count))
                if count == k:
                    stack = stack[:- k]
                    count = 1
            else:
                count = 1
                stack.append((char, count))

        result = ''
        for tup in stack:
            result += tup[0]
        
        return result
