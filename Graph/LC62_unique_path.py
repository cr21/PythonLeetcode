"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down



"""

# APPROACH 1:

# TOP DOWN


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m==1 and n==1:
            return 1
        
        memo={}
        def dfs(m, n):
            
            if (m,n) in memo:
                return memo[(m,n)]
            
            if m == 0 and n == 0:
                return 0
            
            if m == 0 or n==0:
                return 1
            
            memo[(m,n)]= dfs(m-1,n) + dfs(m, n-1)
            return memo[(m,n)]
        
        return dfs(m-1, n-1)
      
      
  # BOTTOM UP 
  
  class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m  <=1 and n <=1 :
            return 1
        dp = [[0]*n]*m
        
        for row in range(1,m):
            dp[row][0]=1
        for col in range(1,n):
            dp[0][col] = 1
            
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        

