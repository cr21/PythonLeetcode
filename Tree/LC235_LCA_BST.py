"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root :
            return None
        
        # if we ever found any of the node p or q return it
        # as we know we reach any of the node , other node should be in descendent of that root
        if root.val == p.val or root.val == q.val:
            return root
        
        p_left=False
        q_left = False
        
        if p.val <  root.val:
            p_left = True
            
        if q.val < root.val:
            q_left = True
        # if q and p are different side of current root return current root
        if (q_left and not p_left) or (p_left and not q_left) :
            return root
        
        # if both p and q are left side of current root
        # return lowest lca of current root left subtree
        if p_left and q_left:
            return  self.lowestCommonAncestor(root.left, p,q)
        # if both p and q are right side of current root
        # return lowest lca of current root right subtree
        if not p_left and  not q_left:
            return  self.lowestCommonAncestor(root.right, p,q)
        
        return root
        
        
        

