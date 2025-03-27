class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = set()
        for i in range(26):
            check.add(chr(ord('a') + i))
        heap, visited = [], set()
        for char in s:
            if char not in check and char not in visited:
                visited.add(char)
                heappush(heap, -int(char))
        
        if len(heap) <= 1:
            return -1
        maxx = -heappop(heap)
        result = -heappop(heap)
        
        if maxx == result:
            return -1
        
        return result

        

        