class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n, m = len(mat), len(mat[0])
        result = defaultdict(list)
        temp = 0

        for row in range(n):
            for col in  range(m):
                result[row+col].append(mat[row][col]) 

        final_result = []
        for idx, list_ in result.items():
            if idx%2 == 0:
                for num in list_[::-1]:
                    final_result.append(num)
            else:
                for num in list_:
                    final_result.append(num)

        return final_result



        