class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = set(), defaultdict(int)
        result = [[] for _ in range(2)]
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        
        for winner in winners:
            if winner not in losers:
                result[0].append(winner)
        
        for loser, freq in losers.items():
            if freq == 1:
                result[1].append(loser)
        
        for res in result:
            res.sort()
        
        return result