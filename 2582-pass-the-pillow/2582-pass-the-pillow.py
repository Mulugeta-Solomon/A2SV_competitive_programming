class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        count = 1
        flag = True
        while time > 0:
            if flag:
                count += 1
                if count == n:
                    flag = False
                    time -= 1
                    continue 
            if not flag:
                count -= 1
                if count == 1:
                    flag = True
            time -= 1
        
        return count
            


        