"""
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.


"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = {c:set() for word in words for c in word}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1)> len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # find first non matching chars and build graph
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
                    
        visited={} # False For visited, True == in Current PAth
        res=[]
        
        def dfs(c):
            if c in visited:
                return visited[c]
            
            # mark 
            visited[c]=True
            for neigh in graph[c]:
                # cycle
                if dfs(neigh):
                    return True
            
            # unmark 
            visited[c]=False
            # post order dfs
            res.append(c)
            
        for c in graph:
            if dfs(c):
                return ""
        
        return "".join(res[::-1])
            
            
            
