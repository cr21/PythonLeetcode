"""

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        if not preorder or len(preorder)==0:
            return None
        
            
        
        def dfs(inorder, preorder):
            print("dfs called")
            if len(inorder)==0 or len(preorder)==0:
                return None
            
            root = TreeNode(preorder[0])
            inIndex = -1
            for id,ele in enumerate(inorder):
                if ele == preorder[0]:
                    inIndex=id
            
            
            preLeft = preorder[1:inIndex+1].copy()
            preRight = preorder[inIndex+1:].copy()
            inLeft = inorder[0:inIndex].copy()            
            inRight = inorder[inIndex+1:].copy()
            
            root.left = dfs(inLeft, preLeft)
            root.right = dfs(inRight, preRight)
            
            return root
        return dfs(inorder, preorder)
        # APPAROCH 2 Optimized approach
        
            
        print("###")
        
        index = 0
        def buildTree(start, end):
            nonlocal index
            if start > end:
                return None
            
            root = TreeNode(preorder[index])
            
            inIndex = indict.get(preorder[index])
            index+=1
            
            root.left = buildTree( start, inIndex-1)
            
            root.right = buildTree( inIndex+1, end)
            
            return root
        
        index=0
        
        return buildTree( 0, len(inorder)-1)
            
