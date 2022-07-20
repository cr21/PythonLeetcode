"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        
#         def dfs(row, col, index):
#             # if Cell is already used for forming word we can not reuse it again
#             if row < 0 or row >= m or col <  0 or  col >= n or board[row][col]=='#':
#                 return False
            
#             # if we reached end of index return True we found word
#             if index == len(word):
#                 return True
            
#             # book keeping original value of current cell
#             prev = board[row][col]
            
#             # mark visited current cell
#             board[row][col]='#'
            
#             # iterate over neighbors
#             for d in [[1,0],[0,1],[-1,0],[0,-1]]:
#                 new_r = row+d[0]
#                 new_c = col+d[1]
#                 # if in limit and character at index matches the character in original word then run dfs recursively
#                 if new_r >=0 and new_r < m and new_c>=0 and new_c <n and  board[new_r][new_c] == word[index]:
#                     if dfs(new_r, new_c, index+1):
#                         return True
                    
#             # unvisted again
#             board[row][col] = prev
#             return False

        def dfs_2(row, col, suffix):
            if len(suffix) == 0:
                return True
            
            if row <0 or row >= m or col <0 or col >=n or board[row][col]!=suffix[0]:
                
                return False
            
            flag = False
            board[row][col] = '#'
            for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                new_r = row+d[0]
                new_c = col + d[1]
                
                flag = dfs_2(new_r, new_c, suffix[1:])
                if flag:
                    return True
                
            # move back original value
            # backtrack
            board[row][col]=suffix[0]
            
            return False
            
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs_2(i,j,word):
                        return True
        return False
