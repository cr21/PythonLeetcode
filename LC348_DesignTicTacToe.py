"""

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
 

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
 

Constraints:

2 <= n <= 100
player is 1 or 2.
0 <= row, col < n
(row, col) are unique for each different call to move.
At most n2 calls will be made to move.
 

Follow-up: Could you do better than O(n2) per move() operation?
"""



# Approach 1 using Dictionary

class TicTacToe:

    def __init__(self, n: int):
        self.player1 = 1
        self.player2 = -1
        self.isGameOver = False
        self.winner = 0
        self.moveX = {
                        'rows':{},
                        'cols':{},       
                     }
        self.moveY = {
                        'rows':{},
                        'cols':{},   
                    }
        
        self.diagonal = 0
        self.antiDiagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        
        current_player = 1 if player==1 else -1
        # make move
        if player == 1:
            if row not in self.moveX['rows']:
                self.moveX['rows'][row]=0
            if col not in self.moveX['cols']:
                self.moveX['cols'][col]=0   
            self.moveX['rows'][row]+=1
            self.moveX['cols'][col]+=1
            
            # check in rows and column if we find winner
            if self.moveX['rows'][row] == self.n or self.moveX['cols'][col] == self.n :
                self.isGameOver = True
                self.winner = 1  
                return 1
            
            
#             check for diagonal

            if row == col: 
                self.diagonal += current_player

            # Update anti diagonal
            if col == (self.n - row - 1): 
                self.antiDiagonal += current_player
                
            if abs(self.diagonal) == self.n or abs(self.antiDiagonal) == self.n:
                return 1

        else:
            # Player 2
            if row not in self.moveY['rows']:
                self.moveY['rows'][row]=0
            if col not in self.moveY['cols']:
                self.moveY['cols'][col]=0   
            self.moveY['rows'][row]+=1
            self.moveY['cols'][col]+=1
            
            # check in rows and columns for winner
            if self.moveY['rows'][row] == self.n or self.moveY['cols'][col] == self.n :
                self.isGameOver = True
                self.winner = 2 
                return 2
            
            if row == col: 
                self.diagonal += current_player

            # Update anti diagonal
            if col == (self.n - row - 1): 
                self.antiDiagonal += current_player
                
            if abs(self.diagonal) == self.n or abs(self.antiDiagonal) == self.n:
                return 2
        
        
        
        
        return 0
        
            
            
            
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
