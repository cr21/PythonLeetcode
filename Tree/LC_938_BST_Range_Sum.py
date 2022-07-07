"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        inlist=[]
        output=[]
        def inorder(root):
            
            if not root:
                return
            # if current root is in range of low and high do inorder traversal
            if root.val >= low:
                inorder(root.left)
            # if current root val is with in limit of low and high
            # add it to output
            if root.val >= low and root.val <= high:
                output.append(root.val)
                
            inlist.append(root.val)
            if root.val <= high:
                inorder(root.right)
            
            
        inorder(root)
        
        
        return sum(output)
            

     ans = 0
     stack=[root]
     while stack:
         node = stack.pop()
         if node:
             if node.val >= low and node.val <= high:
                 ans+=node.val
             if node.val >= low:
                 stack.append(node.left)
             if node.val <= high:
                 stack.append(node.right)

     return ans

