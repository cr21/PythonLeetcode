"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        current_window_best=0
        current_window_length = 0
        counter = {}
        # A A B A B B B
        
        while right < len(s):
            ch = s[right]
            counter[ch] = counter.get(ch,0)+1
            # which char has maximum frequency in current windo
            current_window_best = max(current_window_best, counter.get(ch))
            
            # update current window length
            current_window_length = right-left+1
            
            # if there are some room for character to change then change it
            
            if current_window_length - current_window_best > k :
                left_ch = s[left]
                counter[left_ch] = counter.get(left_ch)-1
                left+=1
                
            max_len = max(max_len,right-left+1)
            
            right+=1
            
        return max_len
       
       
       
       class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # APPROACH 1 :O(N)
#         left = 0
#         right = 0
#         max_len = 0
#         current_window_best=0
#         current_window_length = 0
#         counter = {}
#         # A A B A B B B
        
#         while right < len(s):
#             ch = s[right]
#             counter[ch] = counter.get(ch,0)+1
#             # which char has maximum frequency in current windo
#             current_window_best = max(current_window_best, counter.get(ch))
            
#             # update current window length
#             current_window_length = right-left+1
            
#             # if there are some room for character to change then change it
            
#             if current_window_length - current_window_best > k :
#                 left_ch = s[left]
#                 counter[left_ch] = counter.get(left_ch)-1
#                 left+=1
                
#             max_len = max(max_len,right-left+1)
            
#             right+=1
            
#         return max_len

        # APPROACH 2 O(26*N)
        
        left = 0
        res=0
        counter={}
        max_freq_element = 0
        
        for right in range(len(s)):
            rchar = s[right]
            counter[rchar]= 1 + counter.get(rchar,0)
            
            # maximum replacement that could have been allowed
            while  (right-left+1) - max(counter.values())  > k :
                lchar = s[left]
                counter[lchar]-=1
                
                left+=1
                
            res = max(res, right-left+1)
            
        return res
                
        
        
        
        
