class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for astroid in asteroids:          # [5,10,-5], [10,2,-5], [8,-8], [1,-1, 1,-5]
            if not stack:
                stack.append(astroid)
                continue 
                
            if astroid < 0:
                while stack:
                    if stack[-1] < 0:     
                        stack.append(astroid)
                        break
                    if abs(astroid) > stack[-1]:
                        stack.pop()
                        if not stack:
                            stack.append(astroid)
                            break
                    elif abs(astroid) < stack[-1]:
                        break
                    else:
                        stack.pop()
                        break

            else:
                stack.append(astroid)
            
        return stack
