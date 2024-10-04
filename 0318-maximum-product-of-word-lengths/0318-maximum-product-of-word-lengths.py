class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookUp = [set(words[i]) for i in range(len(words))]
        result = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (lookUp[i] & lookUp[j]):
                    result = max(result, len(words[i]) * len(words[j]))
        
        return result