class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        look_up = defaultdict(tuple)
        rows, cols = len(mat), len(mat[0])
        row, col = [cols] * rows, [rows] * cols

        for r in range(rows):
            for c in range(cols):
                look_up[mat[r][c]] = (r, c)
        
        for i, num in enumerate(arr):
            r, c = look_up[num]
            row[r] -= 1
            col[c] -= 1
            if row[r] == 0 or col[c] == 0:
                return i