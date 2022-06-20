"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp =[[0 for j in range(m+1)] for i in range(n+1)]
    
        for i in range(n+1):
            dp[i][0] = i
        
        for j in range(m+1):
            dp[0][j] = j

        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                # delete char from word 1
                a  = dp[i-1][j]
                # add char to word 1
                # ideally it should be dp[i+1][j]
                # but we don't have information for dp[i+1]
                # so adding character to word1 is equvivlatent to delete char from word2
                
                # we dont have information
                b = dp[i][j-1]
                # replace char from word1
                c = dp[i-1][j-1]
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] =1 +  min(a,min(b,c-1))
                elif word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(a, min(b,c))
                    
        return dp[n][m]
