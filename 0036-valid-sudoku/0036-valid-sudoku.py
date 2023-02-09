class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    if cur in sudoku[(i//3,j//3)]:
                        return False
                    sudoku[(i//3,j//3)].add(cur)
        
        for row in board:
            tmp = [elem for elem in row if elem != '.']
            if len(tmp) != len(set(tmp)):
                return False
        
        board_T = list(zip(*board))
    
        for row in board_T:
            tmp = [elem for elem in row if elem != '.']
            if len(tmp) != len(set(tmp)):
                return False
                
                
        return True