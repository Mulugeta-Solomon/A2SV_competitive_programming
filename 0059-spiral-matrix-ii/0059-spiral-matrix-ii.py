class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        val = 1
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result[top][col] = val
                val += 1
            top += 1

            for row in range(top, bottom + 1):
                result[row][right] = val
                val += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result[bottom][col] = val
                    val += 1
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result[row][left] = val
                    val += 1
                left += 1
        
        return result

        