class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        curr_sum = 0
        i = 1

        while i * i <= num:
            if num % i == 0:
                curr_sum += i
                if i * i != num:
                    curr_sum += num // i
            i += 1
        
        return curr_sum - num == num
