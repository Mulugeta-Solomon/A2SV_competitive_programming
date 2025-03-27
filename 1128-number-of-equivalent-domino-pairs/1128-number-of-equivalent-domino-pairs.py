class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        lookup, result = defaultdict(int), 0
        for a, b in dominoes:
            if (a, b) in lookup:
                lookup[(a, b)] += 1
                continue
            if (b, a) in lookup:
                lookup[(b, a)] += 1
                continue
            
            lookup[(a, b)] += 1
        
        for k, v in lookup.items():
            if v > 1:
                result += (v * (v - 1)) // 2
        
        return result