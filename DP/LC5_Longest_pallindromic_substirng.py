"""

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        
        # APPROACH 1
#         def expandAroundCenter(left, right,s):
#             nonlocal st
#             nonlocal end
#             while left >=0 and right < len(s) and s[left] == s[right]:
#                 left-=1
#                 right+=1
                
#             # keep in bound
#             left+=1
#             right-=1
            
#             if (right -left) > (end-st):
#                 st = left
#                 end = right
                
            
                
            
#         for index in range(len(s)):
#             expandAroundCenter(index, index,s)
#             expandAroundCenter(index, index+1,s)
            
#         return s[st:end+1]

        # APPROACH 2
        st = 0
        end = 0
        if not s:
            return ""
        
       
        def lps(s,left,right):
            while left>=0 and right< len(s) and s[left]==s[right]:
                left-=1
                right+=1
                
            return right-left-1
        
        
        
        for index in range(len(s)):
            
            len1= lps(s, index, index)
            len2 = lps(s,index, index+1)
            
            max_len = max(len1, len2)
            
            if max_len > (end-st):
                
                #left index is current index - out_len/2
                
                st = (index - (max_len - 1)  // 2)
                #right index is current index + out_len/2
                end = (index + max_len // 2)
                
        return s[st:end+1]
                
            
    
            
        
            
            
            
        
        
        
