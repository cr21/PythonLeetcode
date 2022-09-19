"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        last_pos = len(nums)-1
        
        for pos in range(last_pos-1,-1,-1):
            if pos + nums[pos] >= last_pos:
                last_pos = pos
        return last_pos == 0
         # DP
            
        
#         if len(nums)<=1:
#             return True
        
#         dp = [0]*len(nums)
#         # last state is reachable
#         dp[-1]=1
        
#         def backtrack(index):
#             if dp[index]!=0:
                
#                 if dp[index]== 1:
#                     return True
                
#                 return False
            
#             max_jump_index = min(index+nums[index], len(nums)-1)
            
#             for i in range(max_jump_index, index,-1):
                
#                 if backtrack(i):
#                     dp[index]=1
#                     return True
#             dp[index]=-1
#             return False
        
#         return backtrack(0)
        
    
        
