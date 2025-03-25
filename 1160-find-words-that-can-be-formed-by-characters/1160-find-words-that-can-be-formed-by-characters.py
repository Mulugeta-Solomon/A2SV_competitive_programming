class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        lookup, result = Counter(chars), 0
        for word in words:
            curr = len(word)
            word = Counter(word)
            flag = True
            for k, v in word.items():
                if lookup[k] < v:
                    flag = False
                    break
            if flag:
                result += curr
        
        return result

        

        