class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        freq = Counter(word)
        
        for char in freq:
            freq[char] -= 1
            if freq[char] == 0:
                freq.pop(char)

            if len(set(freq.values())) == 1:
                return True

            freq[char] += 1
        
        return False