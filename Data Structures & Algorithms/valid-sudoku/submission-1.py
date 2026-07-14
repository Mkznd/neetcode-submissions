from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_nums = [i for i in row if i != "."]
            if len(set(row_nums)) != len(row_nums):
                return False

        cols = [0] * 9

        for i in range(9):
            cols[i] = [r[i] for r in board if r[i] != "."]
        
        if any([len(set(c)) != len(c) for c in cols]):
            return False

        boxes = defaultdict(lambda: [])

        for i in range(9):
            for j in range(9):
                box_index = (i//3, j//3)
                if board[i][j] != '.':
                    boxes[box_index].append(board[i][j])
                
            
        for i in boxes.values():
            if len(set(i)) != len(i):
                return False

        return True

