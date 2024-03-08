class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n, m = len(mat), len(mat[0])
        diag_values = defaultdict(list)

        for row in range(n):
            for col in  range(m):
                diag_values[row+col].append(mat[row][col]) 

        result = []
        for idx, list_ in diag_values.items():
            if idx%2 == 0:
                for num in list_[::-1]:
                    result.append(num)
            else:
                for num in list_:
                    result.append(num)

        return result



        