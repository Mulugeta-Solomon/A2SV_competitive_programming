class Solution:
    def countVowelStrings(self, n: int) -> int:
        return int(math.factorial(5 + n - 1) / (math.factorial(n) * math.factorial(4)))
        