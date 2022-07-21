"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # APPROCH 1 TLE
#         m = len(text1)
#         n = len(text2)
        
        
#         def helper(s1, s2, i, j):
            
#             if i <0 or j <0:
#                 return 0
            
#             if s1[i] == s2[j]:
#                 return 1 + helper(s1,s2,i-1,j-1)
            
#             else:
#                 return max(
#                     helper(s1,s2,i,j-1),
#                     helper(s1,s2,i-1,j)
#                 )
#         return helper(text1, text2, m-1,n-1)

        m = len(text1)
        n = len(text2)
        # APPROACH 2
        
#         dp = [[0]*(n+1) for i in range(m+1)]
#         # print(len(dp), len(dp[0]))
        
#         for col in range(n):
#             for row in range(m):
#                 if text2[col] ==  text1[row]:
#                     dp[row+1][col+1]= 1+ dp[row][col]
#                 else:
#                     dp[row+1][col+1] = max(dp[row][col+1], dp[row+1][col])
                    
#         return dp[m][n]

        # APPROACH 3
    
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for row in range(len(text1)-1,-1,-1):
            for col in range(len(text2)-1,-1,-1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row][col+1],dp[row+1][col])
        return dp[0][0]
            



                
