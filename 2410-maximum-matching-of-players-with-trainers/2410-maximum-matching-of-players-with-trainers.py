class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        player_ptr, trainer_ptr, max_matching = 0, 0, 0

        while player_ptr < len(players) and trainer_ptr < len(trainers):

            if players[player_ptr] <= trainers[trainer_ptr]:
                max_matching += 1
                player_ptr += 1
                trainer_ptr += 1
            else:
                trainer_ptr += 1
        
        return max_matching
        