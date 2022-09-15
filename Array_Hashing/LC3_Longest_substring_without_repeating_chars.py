"""
Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        n = len(s)
        
        left = 0
        right=0
        _map =dict()
        n = len(s)
        
        max_len = 1
        while right < n:
            rch =s[right]
            # if char is already in map
            # put left pointer to the index one greater than previous occurance index of element
            if rch  in _map:
                left = max(_map[rch]+1,left)
            # update maxlength
            max_len = max(max_len, right-left+1)
            _map[rch] = right
            
            
            right+=1
        return max_len
