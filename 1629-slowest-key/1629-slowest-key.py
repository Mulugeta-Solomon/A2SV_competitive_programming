class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        result, maxx = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] > maxx:
                maxx = releaseTimes[i] - releaseTimes[i - 1]
                result = keysPressed[i]
            if releaseTimes[i] - releaseTimes[i - 1] == maxx and keysPressed[i] > result:
                result = keysPressed[i]
        
        return result

        