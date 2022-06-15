"""

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
 

Constraints:

m == maze.length
n == maze[i].length
1 <= m, n <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= m
0 <= startcol, destinationcol <= n
Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
The maze contains at least 2 empty spaces.

"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        
        dirs= [[-1,0],[1,0],[0,1],[0,-1]]
        
        self.destination = destination
        visited = [[False for i in range(len(maze[0]))]for j in range(len(maze))]
        def dfs(maze, visited,r,c):
            
            if  visited[r][c]:
                return False
            
            if r == self.destination[0] and c == self.destination[1]:
                return True
            visited[r][c] = True
            
            right,left,up,down = c +1, c-1,  r-1, r+1
            
            # up
            
            while up >=0 and maze[up][c] == 0:
                up-=1
                
            if dfs(maze, visited, up+1,c):
                return True
            
            # down
            
            while down < len(maze) and maze[down][c] == 0:
                down+=1
                
            if dfs(maze, visited, down-1,c):
                return True
            
            # right
            
            while right < len(maze[0])  and maze[r][right] == 0:
                right+=1
                
            if dfs(maze, visited, r, right-1):
                return True
            
            # left
            while left >=0 and maze[r][left]==0:
                left-=1
                
            if dfs(maze, visited, r,left+1):
                return True
            
            
            return False
            
            
        return dfs(maze, visited,start[0], start[1])
        
            
            
            
# Approach 2 BFS
        
      queue = deque()
      queue.appendleft(start)
      #mark visited
      visited[start[0]][start[1]] = True

      while queue:
          point = queue.popleft()

          if point[0]==self.destination[0] and point[1]==self.destination[1]:
              return True

          for _dir in dirs:
              newR = point[0]+_dir[0]
              newC = point[1]+_dir[1]

              while ( newR >=0 and newR <len(maze) and newC>=0 and newC<len(maze[0]) and maze[newR][newC]==0):
                  newR+=point[0]
                  newC+=point[1]

              if  visited[newR-point[0]][newC-point[1]] == False:
                  queue.append([newR-point[0],newC-point[1]])
                  visited[newR-point[0]][newC-point[1]]=True

      return False
