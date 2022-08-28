"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # APPROACH 1
        # SORTED KEY WITH. HASH MAP
        
#         mapper = dict()
        
#         for s in strs:
#             sorted_str = "".join(sorted(s))
#             if sorted_str not in mapper:
#                 mapper[sorted_str]=[]
#             mapper[sorted_str].append(s)

        
#         return  [V for K,V in mapper.items()]

        # APPRAOCH 2
    
        ans =collections.defaultdict(list)
        
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
        
#         return ans.values()
    
        # APPROACH 3
        
        ans =collections.defaultdict(list)
        
        for s in strs:
            counter = [0]*26

            for c in s:
                counter[ord(c)-ord('a')]+=1
                
            ans[tuple(counter)].append(s)
            
        return ans.values()
                
       
