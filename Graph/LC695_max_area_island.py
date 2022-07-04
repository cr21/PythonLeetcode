"""


You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

# BFS:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        
        def bfs(row, col, visited):
            if (row, col) in visited:
                return
            grid[row][col]=0
            visited.add((row, col))
            
            for _dir in [[1,0],[0,1],[-1,0],[0,-1]]:
                newR = row + _dir[0]
                newC = col + _dir[1]
                
                if newR >=0 and newR < m and newC >=0 and newC < n and (newR, newC) not in visited and grid[newR][newC]==1: 
                    bfs(newR, newC, visited)
        
        
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    visited=set()
                    
                    bfs(i,j, visited)
                    max_area = max(max_area, len(visited))
        return max_area
        
