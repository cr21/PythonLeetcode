"""

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            
            if self.prev != None and self.prev.val >= root.val:
                return False
            self.prev = root
            
            return inorder(root.right)
            
            
            
        return inorder(root)
#         if root is None:
#             return True
        
#         stack =[]
#         self.prev = None
        
#         while root != None or len(stack) >0:
#             # print(root)
#             # nonlocal prev
            
#             while root :
#                 # nonlocal prev
#                 stack.append(root)
#                 root = root.left
                
#             root = stack.pop()
            
#             if self.prev != None and  self.prev.val >= root.val:
#                 return False
            
#             self.prev = root
            
#             root= root.right
            
#         return True
        
#         def dfs(root, minVal=None,maxVal=None):
#             if root is None: 
#                 return True
            
#             if minVal !=  None and root.val <= minVal:
#                 return False
            
#             if maxVal !=None and root.val >= maxVal:
#                 return False
            
#             return dfs(root.left, minVal, root.val) and dfs(root.right, root.val,maxVal)
        
        
#         return dfs(root)
            
#         prev = None
#         def dfs(root):
#             nonlocal prev
#             if root is None:
#                 return True
            
#             left_result = dfs(root.left)
#             if not left_result:
#                 return False
            
#             if prev !=None and not (prev.val < root.val):
#                 return False
             
#             prev = root
#             return dfs(root.right)
        
        
#         return dfs(root)
        


        
