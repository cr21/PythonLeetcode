"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # APPROACH 1 : TWO MAP 
#         if not s or not t:
#             return False
        
#         if len(s)!=len(t):
#             return False
        
#         set1 = Counter(s)
        
#         set2=Counter(t)
        
        
#         for key in set1:
#             if key not in set2 :
#                 return False
#             if set1[key] != set2[key]:
#                 return False
            
#         return True
        
    
    # APPROACH 2 : Single Map
        if not s or not t:
            return False
        
        if len(s)!=len(t):
            return False
        
        set1 = Counter(s)
        
        
        for ch in t:
            if ch not in set1 :
                return False
            set1[ch]-=1
            if set1[ch] == 0:
                del set1[ch] 
            
            
        return len(set1)==0
        
        
        
            
        
        
        
        
            
        
        
