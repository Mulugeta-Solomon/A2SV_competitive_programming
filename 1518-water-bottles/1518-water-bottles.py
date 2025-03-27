class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result, rem = numBottles, 0
        while numBottles >= numExchange :
            rem = numBottles % numExchange
            numBottles //= numExchange
            result += numBottles
            numBottles += rem
        
        return result
        