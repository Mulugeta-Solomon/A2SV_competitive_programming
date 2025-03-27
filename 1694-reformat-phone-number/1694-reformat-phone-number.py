class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        
        number = ''.join(number.split('-'))
        number = ''.join(number.split(' '))
        result = []
        
        while number:
            if len(number) == 2:
                result.append(number)
                break
            if len(number) == 4:
                result.append(number[:2])
                result.append(number[2:])
                break
            result.append(number[:3])
            number = number[3:]

        return '-'.join(result)