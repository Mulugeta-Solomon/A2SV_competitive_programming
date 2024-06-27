class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([("0000", 0)])

        if "0000" not in deadends:
            deadends.add("0000")
        
        while queue:
            curr, move = queue.popleft()

            if curr == target:
                return move 
            
            for i in range(4):
                # Rotate CW
                next_comb = curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i+1:]
                if next_comb not in deadends:
                    deadends.add(next_comb)
                    queue.append((next_comb, move + 1))
                
                # Rotate CCW
                next_comb = curr[:i] + str((int(curr[i]) - 1) % 10) + curr[i+1:]
                if next_comb not in deadends:
                    deadends.add(next_comb)
                    queue.append((next_comb, move + 1))
        
        return -1

