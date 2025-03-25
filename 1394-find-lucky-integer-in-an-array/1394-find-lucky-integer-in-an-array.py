class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lookup, result = Counter(arr), -1

        for key, val in lookup.items():
            if key == val:
                result = max(result, val)
        
        return result