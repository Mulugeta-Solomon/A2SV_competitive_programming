class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        lookUp = defaultdict(int)

        for i in range(len(matrix)):
            curr = matrix[i]
            if curr[0]:
                curr = [0 if val else 1 for val in curr]

            lookUp[tuple(curr)] += 1

        return max(lookUp.values())


