class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        lookUp, result = defaultdict(int), [0] * len(words)

        for word in words:
            curr = ''
            for char in word:
                curr += char
                lookUp[curr] += 1
                
        for i, word in enumerate(words):
            curr, score = '', 0
            for char in word:
                curr += char
                if curr in lookUp:
                    score += lookUp[curr]

            result[i] = score

        return result


