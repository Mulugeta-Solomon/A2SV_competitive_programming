class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = float('-inf')
        for i in range(len(num)):
            if int(num[i]) % 2:
                result = num[:i+1]
        
        return result if result != float('-inf') else ''
        