"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo=dict()
        def dfs(index):
            # if index in cache return it
            if index in memo:
                return memo[index]
            # if we reach end of string return True
            if index >= len(s):
                return True
            
            # iterate over each word and see if current string startswith that word
            for word in wordDict:
                if s[index:].startswith(word):
                    # change index to next index word we want to check for
                    index = index+len(word)
                    # recurse over next index
                    if dfs(index):
                        memo[index]=True
                        return True
                    # backtrack if previous index won't work
                    index -=len(word)
                    
            memo[index]=False
            return False
        
        return dfs(0)
