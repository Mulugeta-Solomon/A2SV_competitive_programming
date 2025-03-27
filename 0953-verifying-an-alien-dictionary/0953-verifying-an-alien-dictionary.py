class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        lookup = defaultdict(int)
        for i in range(len(order)):
            lookup[order[i]] = i
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:                
                    if lookup[words[i][j]] > lookup[words[i + 1][j]]:
                        return False
                    break
        return True