"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000

"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        ## APPRAOCH 1 TLE (M^N) M = # coins
#         def backtrack(coins, index, amount, total):
#             # nonlocal res
#             if index >=len(coins) or total > amount:
#                 return 0
#             if amount == total:
                
#                 return 1
            
#             for i in range(index,len(coins)):
#                 # choose 
#                 case1 = backtrack(coins, i, amount,total+coins[index])
#                 # not choose
                
#                 case2 = backtrack(coins, i+1, amount,total)
                
#                 return case1+case2
            
        
#         return backtrack(coins, 0, amount, 0)

        # APPROACH 2 TOP DOWN CACHING O(M*N)
    
#         cache = {}
#         def backtrack(coins, index, amount, total):
#             if index >=len(coins) or total > amount:
#                 return 0
            
#             if amount == total:
#                 return 1
            
#             # check in cache
#             if (index, total) in cache:
#                 return cache[ (index, total)]
            
            
#             # choose 
#             case1 = backtrack(coins, index, amount,total+coins[index])

#             # not choose

#             case2 = backtrack(coins, index+1, amount,total)
            
#             # cache the result
#             cache[ (index, total)] = case1+case2
            
#             return case1+case2
            
        
#         return backtrack(coins, 0, amount, 0)
        
        # BOTTOM UP DP
        
#         dp = [0]*(amount+1)
#         dp[0]=1
        
#         for coin in coins:
#             for amt in range(coin, amount+1):
#                 dp[amt] =dp[amt]+ dp[amt-coin]
#         return dp[amount]

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                # not Choose case
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    # choose case
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                # not choose case
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    # choose case
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
        
        
        
        
        
        
                
