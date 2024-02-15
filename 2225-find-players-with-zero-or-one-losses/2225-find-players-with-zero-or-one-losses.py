class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners = {}
        losers = {}

        for match in matches:
            winner, loser = match[0], match[1]

            if winner not in winners:
                winners[winner] = 1
            else:
                winners[winner] += 1

            if loser not in losers:
                losers[loser] = 1
            else:
                losers[loser] += 1

        result = [[],[]]

        for key, value in winners.items():
            if key not in losers:
                result[0].append(key)
        
        for key, value in losers.items():
            if value == 1:
                result[1].append(key)
        
        for sublist in result:
            sublist.sort()
        
        return result
