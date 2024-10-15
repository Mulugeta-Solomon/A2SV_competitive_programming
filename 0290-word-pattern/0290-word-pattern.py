class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        if len(set(s.split(' '))) != len(set(pattern)) or len(s.split(' ')) != len(pattern):
            return False

        lookUp = defaultdict(str)
        s = [char for char in s.split(' ')]

        for i, char in enumerate(pattern):
            if char not in lookUp:
                lookUp[char] = s[i]
                continue
            if lookUp[char] != s[i]:
                return False
        
        return True




        