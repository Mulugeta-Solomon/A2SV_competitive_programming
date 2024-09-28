class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        lookUp = defaultdict(int)

        for card in deck:
            lookUp[card] += 1
        
        if len(lookUp) == 1:
            return lookUp[deck[0]] > 1

        check = lookUp[deck[0]]
        for card, freq in lookUp.items():
            check = gcd(check, freq)
        
        return check > 1

