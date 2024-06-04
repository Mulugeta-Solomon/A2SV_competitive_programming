class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        result = []

        for i in range(1, n + 1):
            curr = [i]
            for j in range(i + 1, n + 1):
                curr.append(j)
                result.append(curr[:])
                curr.pop()
            curr.pop()

        return result