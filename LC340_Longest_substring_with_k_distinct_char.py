"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""

## APPROACH 1:

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0 or len(s)==0 :
            return 0
        left = 0
        right = 0
        current_map = dict()
        max_length = 0
        
        
        while right < len(s):
            
            rchar = s[right]
            if rchar in current_map:
                current_map[rchar]+=1
            else:
                # add it to map
                current_map[rchar] = 1
                while len(current_map)>k:
                    lchar = s[left]
                    current_map[lchar]-=1
                    if current_map[lchar]==0:
                        del current_map[lchar]
                    left+=1
            max_length = max(max_length, right-left+1)
            
            right+=1
        return max_length
       
       
       
# APPROACH 2

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0 or len(s)==0 :
            return 0
        left = 0
        right = 0
        start = 0
        end = 0
        character_map = defaultdict() # character -> its rightmost position
        """
        Maintain the Character map with it's right most position for K distinct values
        Once map size is k+1, remove the character having minimum right most value
        and put left pointer at that position +1
        if current window is larger than previous best update it
        and return it
        
        
        """
        while right < len(s):
            
            character_map[s[right]]=right
            right+=1
            if len(character_map) == k+1:
                min_idx_char = min(character_map.values())
                del character_map[s[min_idx_char]]
                left= min_idx_char+1
            if (right-left) > (end-start):
                end = right
                start = left
                
        return len(s[start:end])
            
