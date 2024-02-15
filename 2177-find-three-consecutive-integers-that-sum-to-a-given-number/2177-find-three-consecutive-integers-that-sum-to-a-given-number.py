class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        temp = (num - 3) / 3

        if floor(temp) == ceil(temp):
            return [int(temp), int(temp) + 1, int(temp) + 2]
        else:
            return []  