"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.

"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m = len(rooms)
        
        if  m ==0:
            return 
        n = len(rooms[0])
        
        OPEN_SPACE =2147483647
        GATE = 0
        WALL = -1
        
        q =deque()
        # we start from the gate
        # we will add all the gates to the queue first
        # and then we will do BFS from the gate it self, it will make sure that 
        # we will always have mininmum distance from the gate
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    q.append((row,col))
                    

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            location = q.popleft()
            r,c = location[0],location[1]
            
            for _d in dirs:
                new_r = r+_d[0]
                new_c = c+_d[1]
                
                if new_r < 0 or new_r >= m or new_c < 0 or new_c >=n or rooms[new_r][new_c] != OPEN_SPACE:
                    continue
                
                rooms[new_r][new_c] = min(rooms[new_r][new_c], 1 + rooms[r][c])
                q.append((new_r, new_c))
                
        
            
