class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in range(len(s)):
            if i % 2:
                result += chr(ord(s[i - 1]) + int(s[i]))
                continue
            result += s[i]
        
        return result

        