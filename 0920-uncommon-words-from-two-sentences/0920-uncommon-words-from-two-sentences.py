class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lookUp1, lookUp2 = defaultdict(int), defaultdict(int)
        result = set()

        for word in s1.split(' '):
            lookUp1[word] += 1
        for word in s2.split(' '):
            lookUp2[word] += 1
        
        for word, freq in lookUp1.items():
            if freq == 1:
                if word not in lookUp2 and word not in result:
                    result.add(word)
        
        for word, freq in lookUp2.items():
            if freq == 1:
                if word not in lookUp1 and word not in result:
                    result.add(word)
   
                
        return [word for word in result]
        