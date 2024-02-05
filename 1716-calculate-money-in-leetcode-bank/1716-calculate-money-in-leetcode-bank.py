class Solution:
    def totalMoney(self, n: int) -> int:
        
        total_save, save_start = 0, 0

        for day in range(n):
            if day%7 == 0:
                save_start += 1
                todays_save = save_start
            
            total_save += todays_save
            todays_save += 1
        
        return total_save

        