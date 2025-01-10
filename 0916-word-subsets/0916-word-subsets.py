class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def count(word):
            result = [0] * 26
            for char in word:
                result[ord(char) - ord('a')] += 1
            return result

        look_up = [0] * 26
        for word in words2:
            curr = count(word)
            for i in range(26):
                look_up[i] = max(look_up[i], curr[i])
        
        result = []
        for word in words1:
            curr, flag = count(word), False
            for i in range(26):
                if curr[i] < look_up[i]:
                    flag = True
            if not flag:
                result.append(word)
        
        return result




        