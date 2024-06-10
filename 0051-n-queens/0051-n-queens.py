class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        

        def isValid(row, col):

            for i in range(n):
                if board[i][col] == 'Q':
                    return False 
                if row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 'Q':
                    return False
                if row - i >= 0 and col + i < n and board[row-i][col+i] == 'Q':
                    return False
            
            return True
        
        def backtrack(row):
            if row == n:
                result.append([''.join(i) for i in board])
                return 
            
            for col in range(n):
                if isValid(row,col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
      
        backtrack(0)

        return result
       