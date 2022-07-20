"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

"""

class TrieNode:
    def __init__(self):
        self.children=dict()
        self.isWord=False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # insert into TRIE
    def insert(self, word):

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]


        node.isWord=True
    
    # SEARCH WORD IN TRIE
    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]
        return node.isWord
    
    # SEARCH IF Any word starts with following prefix
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
            
                
                
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # initialize Trie
        trie = Trie()
        # add all words to Trie Data Structure
        for word in words:
            trie.insert(word)
            
            
        m = len(board)
        n = len(board[0])
        
        result =[]
        def dfs(tree,row, col, word):
            # if you reach to the node where word is present 
            # add it to response
            # isWord
            if tree.isWord:
                result.append(word)
                # mark because we already visisted
                tree.isWord=False
                
            if row >=0 and row < m and col >=0 and col < n  :
                
                char_va = board[row][col]
                # ge next children
                childnode = tree.children.get(char_va)
                # if it is not None
                # we found some matching char,
                # now keep on checking in neighbourhood
                if childnode is not None:
                    word+=char_va
                    # mark visisted
                    board[row][col] = None
                    
                    for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                        r = d[0]+row
                        c = d[1]+col
                        # run dfs over neighbours
                        dfs(childnode,r,c,word)
                    # unmark for next iteration
                    board[row][col]=char_va
                            
            
        for i in range(m):
            for j in range(n):
                if trie.startsWith(str(board[i][j])):
                    dfs(trie.root,i,j,"")
        print(board)
        return result
    
    
    
        ## TLE
        
        
#         m = len(board)
#         n = len(board[0])
        
#         res = []
        
#         def dfs(row, col, index, word):
            
#             if index >= len(word):
#                 return True
            
#             if row < 0 or row >= m or col <  0 or col >= n or board[row][col] == '#':
#                 return False
            
            
#             prev = board[row][col]
            
#             board[row][col]='#'
            
#             for d in [[1,0],[0,1],[-1,0],[0,-1]]:
#                 r1 = d[0]+row
#                 c1= d[1]+col
                
#                 if r1 >=0 and r1<m and c1>=0 and c1 < n and board[r1][c1] == word[index]:
#                     if dfs(r1,c1, index+1, word):
#                         board[row][col]=prev
#                         return True
                    
            
#             board[row][col]=prev
#             return False
            
#         def exists(board, word):
#             for i in range(m):
#                 for j in range(n):
#                     if board[i][j]==word[0]:
#                         if dfs(i,j,1,word):
#                             return True
#             return False
        
        
        
#         for word in words:
#             if exists(board, word):
#                 res.append(word)
#             print(board)
#         return res
