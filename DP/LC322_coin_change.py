"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
#         # Recursive Backtracking Solution
#         if amount == 0:
#             return 0
        
#         memo={}
#         def backtrack(coins, amount, st_index, min_coin):
            
            
#             if st_index >= len(coins):
#                 return float("inf")
            
#             if amount < 0:
#                 return float("inf")
            
#             if amount == 0:
#                 return min_coin
            
#             choose = backtrack(coins, amount-coins[st_index], st_index, min_coin+1)
#             not_choose = backtrack(coins, amount, st_index+1, min_coin)
            
#             # memo[st_index]=min(choose, not_choose)
#             return min(choose, not_choose)
            
#         count = backtrack(coins, amount,0, 0)
#         print(memo)
#         if count== float("inf"):
#             return -1
#         return count

        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        
        # number of coins required to get amount zero with different coins
        
        for index in range(len(dp)):
            dp[index][0] = 0
            
        # number of coins required to get amount using coin with 0th denominations
        for index in range(len(dp[0])):
            dp[0][index]=10000000
        
        
        for row_index in range(1, len(dp)):
            for col_index in range(1, len(dp[0])):
                if col_index < coins[row_index-1]:
                    # you can not choose current coin 
                    dp[row_index][col_index] =  dp[row_index-1][col_index] 
                
                else:    
                    # if we choose the current coin
                    choose = 1 + dp[row_index][col_index - coins[row_index-1]]
                    # if we don't choose the current coin
                    not_choose =  dp[row_index-1][col_index]
                    dp[row_index][col_index] = min(choose, not_choose);
                
                
        return -1 if dp[len(dp) -1] [len(dp[0]) -1 ] >=10000000 else dp[len(dp) -1] [len(dp[0]) -1 ] 
        
        
                
