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
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # # Brute Force
        # count=0
        # # iterate over every substring possible and check if they are pallindromic or not
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         subs = s[i:j+1]
        #         if subs == subs[::-1]:
        #             count+=1
        # return count
        
        
        # Expand around center
        
        ans = 0
        
        def countPallindrome(s, left, right):
            res = 0
            # keep on decrementing left and incrementing right till both left and right
            # index value are same denoting pallindromic behaviour
            # and we increment count by 1 every time condition based on how many times while loop run
            while left >=0 and right < len(s) :
                if(s[left]!=s[right]):
                    break
                left-=1
                right+=1
                res+=1
            return res
            
        
            
        for index in range(len(s)):
            ans+= countPallindrome(s,index,index)
            ans+=countPallindrome(s, index, index+1)
        
        return ans
    
