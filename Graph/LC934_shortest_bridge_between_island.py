"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # Find first Island and Mark all the node belongs to Island 1
        _dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        
        marked = False
        
        m = len(grid)
        n = len(grid[0])
        
        def mark_island1(row, col):
            grid[row][col]=2
            
            for d in _dirs:
                newR = row + d[0]
                newC = col + d[1]
                
                if newR >=0 and newR < m and newC >=0 and  newC < n and grid[newR][newC] ==1:
                    mark_island1(newR, newC)
                    
                    
        # Mark Island 1 nodes
        for i in range(m):
            if not marked:
                for j in range(n):
                    if not marked and grid[i][j] == 1:
                        mark_island1(i,j)
                        marked = True
                        
        print(grid)
                        
        
        
        
                    
        # we have used 2 for marking island 1 node
        # we expand from 2 and at each level during BFS traversal 
        # we will increment mark by 1
        # whenever we encounter 1, we return (mark -2) because we exapnd from 2 to reach
        # to new mark level
        mark = 2
        
        def bfs_expansion(row, col, mark):
            for d in _dirs:
                newR = d[0] + row
                newC = d[1] + col
                
                if newR >=0 and newR < m and newC >=0 and newC < n :
                    # during BFS traversal we found 1 so return it
                    if grid[newR][newC] == 1:
                        return True
                    # if it is zero we would mark as mark number
                    if grid[newR][newC] == 0:
                        grid[newR][newC]=mark
                        
            return False
        
        while True:
            # traverse every row and column with starting mark =2 
            # and each level expand mark 
            for i in range(m):
                for j in range(n):
                    if grid[i][j]== mark and bfs_expansion(i,j,mark+1):
                        return mark-2
            mark+=1
            
        return -1
        
        
