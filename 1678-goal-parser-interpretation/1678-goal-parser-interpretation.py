class Solution:
    def interpret(self, command: str) -> str:
        result, stack = '', []

        for char in command:
            if stack and char == ')':
                if stack[-1] == 'l':
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    result += 'al'
                else:
                    stack.pop()
                    result += 'o'
                continue

            if char == 'G':
                result += char
                continue

            stack.append(char)

        return result 