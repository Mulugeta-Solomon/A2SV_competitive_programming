class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lookUp, result = set(), []

        for word in words:
            for i in range(len(word) + 1):
                for j in range(i + 1, len(word) + 1):
                    if word[i:j] != word:
                        lookUp.add(word[i:j])

        for word in words:
            if word in lookUp:
                result.append(word)
        
        return result
