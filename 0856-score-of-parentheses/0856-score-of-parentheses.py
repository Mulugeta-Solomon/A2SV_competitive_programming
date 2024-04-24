class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        look_up = {')':'('}

        for i in range(len(s)):
            if s[i] not in look_up:
                stack.append(s[i])
            else:
                if stack[-1] == '(':
                    score = 1
                    stack.pop()
                    if stack and stack[-1] != '(':
                        num = stack.pop()
                        stack.append(score + num)
                    else:
                        stack.append(score)
                
                else:
                    multiplier = stack.pop()
                    stack.pop()
                    if stack and stack[-1] != '(':
                        num = stack.pop()
                        stack.append(2 * multiplier + num)

                    else:
                        stack.append(2 * multiplier)

        return stack[0]
                



            

        