"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
         
        # base case 
        # index = 0 :
        
        dp= [0]*(len(cost)+1)
        #base case
        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        
#         for i in range(2, len(cost)+1):
#             one_Step = dp[i-1]+cost[i-1]
#             two_Step = dp[i-2] + cost[i-2]
            
#             dp[i] = min(one_Step, two_Step)
            
#         # return dp[-1]
        
#         def recurse(index):
#             if index  <=1:
#                 return 0
            
#             if index in memo:
#                 return memo[index]
            
            
#             step1 =  cost[index-1]+ recurse(index-1) 
#             step2 =  cost[index-2]+ recurse(index-2) 
#             memo[index] = min(step1, step2)
#             return memo[index]
#         memo={}
#         return recurse(len(cost))

        
                
    
            
            
