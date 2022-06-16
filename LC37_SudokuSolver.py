"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 
"""


from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        def could_place(d, row, col):
            return not ( d in rows[row] or d in cols[col] or d in boxes[box_index(row,col)]) 
        
        
        def place_number(d, row, col):
            rows[row].add(d)
            cols[col].add(d)
            boxes[box_index(row,col)].add(d)
            board[row][col]=str(d)
            
        
        def remove_number(d,row, col):
            rows[row].remove(d)
            cols[col].remove(d)
            boxes[box_index(row,col)].remove(d)
            board[row][col]='.'
            
        def go_to_next_empty_number(row, col):
            
            if  col == N - 1 and row == N - 1 :
                nonlocal sudokuSolved
                sudokuSolved = True
            else:
                # find the next candidate
                if col == N - 1:
                    backtrack(row + 1,0)
                else:
                    backtrack(row, col + 1)
                
            
        def backtrack(row=0, col=0):
            # if current row and current col has empty cell
            if(board[row][col] == '.') :
                
                for d in range(1,10):
                    # if we could allowed to place number at location
                    if could_place(d, row, col):
                        # place the number
                        place_number(d, row, col)
                        # got to next number if already place number
                        go_to_next_empty_number(row, col)
                        # if after placing to next number sudoku is not solved yet
                        # backtrack
                        if not sudokuSolved:
                            remove_number(d, row, col)
            else:
                # if current cell is not empty go to next empty cell
                go_to_next_empty_number(row, col)
            
        
        n = 3
        N = n * n 
        box_index = lambda row, col: (row//n)*n + col//n
    
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        boxes = defaultdict(set) 
        
        
        
        
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    # place rows cols and boxes dictionary 
                    place_number(d, i, j)
        
        
        sudokuSolved =False
        backtrack()

        
        
        
