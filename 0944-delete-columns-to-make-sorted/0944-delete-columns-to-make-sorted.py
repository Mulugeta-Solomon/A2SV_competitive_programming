class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row, col = len(strs), len(strs[0])

        result = 0
        for i in range(col):
            for j in range(row-1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    result += 1
                    break
        return result



        