class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for e in expression:
            if e != ')' and e != ',':
                stack.append(e) # valid expression to the stack 
            
            if e == ')': # evaluate 
                curr = []

                while stack and stack[-1] != '(': # pop until '('
                    t = stack.pop()
                    curr.append(True if t == 't' else False)
                
                stack.pop()

                if stack:
                    opr = stack.pop() # operator 
                    v = curr[0]

                    if opr == '&':
                        for b in curr:
                            v &= b
                    elif opr == '|':
                        for b in curr:
                            v |= b
                    else:
                        v = not v
                    
                    stack.append('t' if v else 'f')
           
        return stack[-1] == 't'
