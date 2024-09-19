class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        n = len(b) // len(a)
        result = 1

        while result <= n + 5:
            if b in a * result :
                return result

            result += 1

        return -1
