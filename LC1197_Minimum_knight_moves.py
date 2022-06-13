"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300


"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        
       
        # solution is symmetric 
        
        #Take the absolute values of the coordinates (x, y).
        # Manually initialize the map with the minimum moves it takes to get to the origin’s coordinates. The map contains the coordinate as the key and minimum knight it takes to get to the origin as the value.
        # Start from the input coordinates and explore all the squares in a depth-first manner back to the origin.
        # If the coordinate has already been explored, we can return that value; otherwise, we will explore the next possible coordinates the knight can move to.
        # We pick the path with the minimum moves and backtrack to the input coordinate.


        x =abs(x)
        y = abs(y)
        
        
        # default moves
        moves = {(0, 0): 0, (1, 1): 2, (2, 0): 2, (0, 2): 2, (1, 0): 3, (0, 1): 3}
        def dfs(x,y):
            
            
            if (x,y) not in moves:
                moves[(x,y)] = min (dfs(abs(x-2),abs(y-1)), dfs(abs(x-1),abs(y-2)))+1
            return moves[(x,y)]
        
        
        
        return dfs(x,y)
    
        
        
        
