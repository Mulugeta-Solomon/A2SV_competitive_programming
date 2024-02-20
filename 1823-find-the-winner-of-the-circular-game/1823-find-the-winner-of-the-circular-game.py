class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = []
        for i in range(1, n+1):
            friends.append(i)
        
        
        pos = 0
        while len(friends) > 1:
            n=len(friends)
            pos=(pos+k-1)%n
            friends.pop(pos)

        return friends[0]

        