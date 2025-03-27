class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        result = ''
        for i in range(len(number)):
            if number[i] == digit:
                curr = number[:i] + number[i+1:]
                if result and int(result) < int(curr):
                    result = curr
                if not result:
                    result = curr 
                    
        return result