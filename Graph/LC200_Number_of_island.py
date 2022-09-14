"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        island_cnt=0
        
        def dfs(row, col):
            # mark visited
            grid[row][col]="2"
            
            for _d in [[1,0],[-1,0],[0,1],[0,-1]]:
                r = row+_d[0]
                c = col + _d[1]
                
                if r >=0 and r < m and c >=0 and c < n and grid[r][c]=="1":
                    dfs(r,c)
        
                
            
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    island_cnt+=1
                    dfs(row, col)
                
        return island_cnt
                    
        
