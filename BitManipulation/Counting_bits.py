"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # APPROACH 1
#         def count_bits(n):
#             mask = 1
#             count = 0
#             for index in range(32):
#                 # for every position slide masking variable and take and 
#                 if n & mask != 0 :
#                     count+=1
#                 # left shift the mask bit 
#                 mask = mask << 1
                
#             return count
    
#         ans = []
#         for num in range(n+1):
#             ans.append(count_bits(num))
#         return ans

#         # APPRAOCH 2
    
#         def popCount(x):
#             count = 0
#             while x != 0:
#                 # e.g x= 3 = 0011  and x-1 == 2 == 0010
#                 # 3 & 2 = 0011 & 0010 = 0010 
#                 # 2 & 1 = 0010 & 0001 = 0000
#                 x &= x-1 # zero out least significant digit
#                 count+=1
#             return count
        
#         ans = [0]*(n+1)
        
#         for num in range(n+1):
#             ans[num] = popCount(num)
            
#         return ans

        # APPRAOCH 3 DP + Least Significant Bit
        dp = [0]*(n+1)
        offset =1
        for x in range(1, n+1):
            if offset*2==x:
                offset=x
            dp[x]=1+dp[x-offset]
        return dp
            

    
        
