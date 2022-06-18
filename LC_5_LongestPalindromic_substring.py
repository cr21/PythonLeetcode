"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "aaccbababcbc"
Output: "cbababc"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.



"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        """
        TLE DP approach
        """
#         if s is "":
#             return s
        
#         dp = [[None for i in range(len(s)) ] for j in range(len(s) )]
#         res=""
#         for j in range(len(s)):
#             for i in range(j+1):
#                 if i == j :
#                     dp[j][i]=True
#                 elif j == i+1 :
#                     dp[j][i] = (s[i]==s[j])
#                 else:
#                     dp[j][i] =dp[j-1][i+1] and (s[i]==s[j])
#                 if dp[j][i] and j-i+1 > len(res):
#                     res = s[i:j+1]
#         return res




+=+++++++++++++++++++++++++++++++  #APPROACH 2 ++++++++++++++++++++++++++++++++++++++  
        ## Optimized expand around center
        ## total 2n-1 centers to consider
        ## O(n^2)

+=+++++++++++++++++++++++++++++++  #APPROACH 2 ++++++++++++++++++++++++++++++++++++++  

        if not s :
            return ""  
        
        start = 0
        end = 0
        
        
        def lps(s,left,right):
            nonlocal start
            nonlocal end
            while left>=0 and right< len(s) and s[left]==s[right]:
                left-=1
                right+=1
            # left and right are already out of bound
            # so make them in bound by correction
            #correction
            left+=1
            right-=1
            if (right-left) > (end-start):
                end=right
                start=left
                
            
        
        for index in range(len(s)):
            lps(s,index,index)
            lps(s,index, index+1)
         
        return s[start:end+1]
                
                
        
