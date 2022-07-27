"""

236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
 
        def dfs(root,n):
            if not root:
                return None
        
            if root == n:
                return [root]
            
            left = dfs(root.left, n)
            right = dfs(root.right, n)
            
            res=[]
            res = left or right
            
            if res:
                res.append(root)
                
            return res
                
        a = dfs(root, p)
        b = dfs(root,q)
        
            
        a= a[::-1]
        b=b[::-1]
        
        ans= None
        for a1,b1 in zip(a,b):
            if a1==b1:
                ans=a1
        def lca(root, p,q):
            
            # return ans
            # print("hi")
            if not root:
                return None

            if root.val == p.val or root.val == q.val:
                return root

            left_lca = lca(root.left, p, q)
            right_lca = lca(root.right, p,q)
            if  left_lca and  right_lca:
                return root
            
            if left_lca:
                return left_lca
            if right_lca:
                return right_lca
            
            return None
        
        return lca(root, p,q)
        
