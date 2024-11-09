class Solution:
    def numSquares(self, n: int) -> int:
        
        queue, result = deque([n]), 0
        possible = min(100, int(sqrt(n)) + 1)

        while queue:
            size = len(queue)
            result += 1
            for _ in range(size):
                curr = queue.popleft()
                
                for val in range(1, possible + 1):
                    if val * val - curr == 0:
                        return result
                    elif curr - val * val > 0:
                        queue.append(curr - val * val)
                    else:
                        break
        return result