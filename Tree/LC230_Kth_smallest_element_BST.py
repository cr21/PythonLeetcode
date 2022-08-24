"""

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive O(N) space, O(LogN) Time
        inlist=[]
        def inorder(root):
            if not root:
                return
            
            # process left subtree
            inorder(root.left)
            # process root
            inlist.append(root.val)
            # process right subtree
            inorder(root.right)
        
        inorder(root)
        return inlist[k-1]
            
#         # APPROACH 1 USING STACK
#         # ITERATIVE APPROACH Time O(K)
#         st = []
        
#         inorder = []
#         while st or root:
#             # process Left Tree
#             while root:
#                 st.append(root)
#                 root = root.left
                
#             root = st.pop()
#             # process root
#             inorder.append(root.val)
            
#             if len(inorder) == k:
#                 return inorder[-1]
            
            
                
#             # go to right
#             root = root.right
            
#         return -1

                
        
