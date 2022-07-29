"""

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        
        ## APPROACH 1
        print("APPROACH 1")
        
        LETTERS = [str(i) for i in range(1, 27)]
        # how manny ways we can decode perticular string
        dp={}
        
        def dfs(s, dp):
            # if string is empty we reached to the end of string by decoidng return 1 Valid way
            
            if s == "" or len(s) == 0:
                return 1
            
            # if string is already cached return from cache
            if s in dp:
                return dp[s]
            
            
            for letter in LETTERS:
                # if current string starts with valid letter
                if s.startswith(letter):
                    dp[s] = dp.get(s, 0) + dfs(s[len(letter):], dp)
                    
            return dp.get(s,0)
        
        return dfs(s, dp)
    
        print("APPROACH 2")
        ## APPROACH 2
        
        memo = {len(s):1}
        
        def dfs(index, memo):
            # return from cache
            if index in memo:
                return memo[index]
            if s[index]=="0":
                return 0
            
            # for 1 digit next char counter ( we have limit from 1-26)
            res = dfs(index+1, memo)
            
            # for 2 digit next char get result
            if ( index +1 < len(s) and 
                (s[index] == "1" or s[index]=="2" and s[index+1] in "0123456" )
               ):
                res+=dfs(index+2, memo)
                
            # cache it
            memo[index]=res
            return res
        
        return dfs(0, memo)
        
            
        
