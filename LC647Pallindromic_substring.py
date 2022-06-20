"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

"""

## BRUTE FORCE

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # Brute Force
        count=0
        # iterate over every substring possible and check if they are pallindromic or not
        for i in range(len(s)):
            for j in range(i,len(s)):
                subs = s[i:j+1]
                if subs == subs[::-1]:
                    count+=1
        return count
