"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        
        m = len(grid)
        n = len(grid[0])
        
        queue = deque()
        fresh_oranges = 0
        total = 0
        for row in range(m):
            for col in range(n):
                # add all rotten orange in queue
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    
                    fresh_oranges+=1
                    
        # if there are no fresh oranges return 0
        
        if fresh_oranges ==0:
            return 0
        
        
        while  queue:
            
            size = len(queue)
            
            total+=1
            # process level
            for index in range(size):
                node = queue.popleft()
                row, col = node[0], node[1]
                
                for dir in dirs:
                    newr = row + dir[0]
                    newc = col + dir[1]
                    
                    if newr >=0 and newr < m and newc >=0 and newc < n and grid[newr][newc] == 1:
                        # mark it as rotten
                        fresh_oranges-=1
                        grid[newr][newc] = 2
                        queue.append((newr, newc))
                        
            if fresh_oranges == 0:
                break
        
        return -1 if fresh_oranges > 0 else  (total )
            
