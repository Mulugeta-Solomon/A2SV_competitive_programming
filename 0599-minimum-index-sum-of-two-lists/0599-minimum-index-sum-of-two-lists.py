class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)

        min_idx = float('inf')
        result = []

        for rest in common:
            idx = list1.index(rest) + list2.index(rest)
            if idx < min_idx:
                min_idx = idx 
                result = [rest]
            elif idx == min_idx:
                result.append(rest)
        
        return result
        