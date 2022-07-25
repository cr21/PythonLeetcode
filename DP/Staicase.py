"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        
        def fibo(n, dp) :
            
            if n<=2:
                dp[n]=n
                return n
            
            if dp[n] != -1:
                return dp[n]
            dp[n] = fibo(n-1,dp) + fibo(n-2, dp)
            return dp[n]
        return fibo(n, dp)
    
