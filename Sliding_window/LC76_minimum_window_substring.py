"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        tmap = collections.Counter(t)
        desired_length = len(tmap)
        matched = 0
        l = 0
        r = 0
        
        current_window=defaultdict(int)
        
        ans = [-1,0,0] # windowlength, left, right end
        
        while r < len(s):
            
            rchar = s[r]
            current_window[rchar]+=1
            
            # if current charcter count is required count in tmap
            
            # we found one character frequency match so increase matching count
            if rchar in tmap and tmap.get(rchar) == current_window[rchar]:
                matched+=1
              
            # now We found answer it's time to contract current window
            
            # need to contract the window, when we find one window having all the charcter in t in that window
            while l <= r and matched == desired_length:
                lchar = s[l]
                if((ans[0]==-1) or (r-l+1 < ans[0]) ):
                    ans=[r - l+1, l, r]
    
    
                current_window[lchar]-=1
                
                # if current window does not contain enought character in string t
                # decrease matching count and increment left pointer
                if lchar in tmap and tmap.get(lchar) > current_window[lchar]:
                    matched-=1
                    
                l+=1
            
            r+=1
            
        return  "" if ans[0] == -1 else  s[ans[1]: ans[2]+1]
                    
                    
                    
            
         
