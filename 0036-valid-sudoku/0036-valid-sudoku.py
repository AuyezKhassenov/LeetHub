class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        for i in range(9):
            box_x = i // 3
            for j in range(9):
                box_y = j // 3
                val = board[i][j]
                if val == '.':
                    continue
                if val in boxes[f"{box_x},{box_y}"]:
                    return False
                boxes[f"{box_x},{box_y}"].add(val)
        
        for row in board:
            row = [val for val in row if val != '.']

            if len(row) != len(set(row)):
                return False
        
        transpose = list(zip(*board))
        for row in transpose:
            row = [val for val in row if val != '.']

            if len(row) != len(set(row)):
                return False
            
        return True