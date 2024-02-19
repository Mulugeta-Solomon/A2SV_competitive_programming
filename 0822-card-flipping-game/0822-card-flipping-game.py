class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        same_side = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])
        min_good_int = float('inf')

        for num in fronts + backs:
            if num not in same_side:
                min_good_int = min(min_good_int, num)
        
        if min_good_int != float('inf'):
            return min_good_int
        
        return 0   