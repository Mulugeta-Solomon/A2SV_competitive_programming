class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        target_dis = abs(target[0]) + abs(target[1])
        
        for i, j in ghosts:
            ghost_target = abs(target[0] - i) + abs(target[1] - j)
            if ghost_target <= target_dis:
                return False
        return True