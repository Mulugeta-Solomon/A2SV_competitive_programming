class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        result = derived[0]
        for val in derived[1:]:
            result ^= val
        
        return result == 0