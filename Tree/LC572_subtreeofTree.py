"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        # if subroot is null it can be subtree of root
        if not subroot:
            return True
        
        # helper function to check if both tree are same
        def isSame(p, q):
            if not p and not q :
                return True
            
            
            if p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right,q.right)
            
            return False
        
        
        # if subroot is subtree of current root check 
        if isSame(root,subroot):
            return True
        
        # check if subroot is subtree of  left part of root or right part of root 
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot);
                
            
        
        
        
        
        
