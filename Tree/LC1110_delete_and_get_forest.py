"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        
        deleted_set = set(to_delete)
        forest = list()
        
        if root is None:
            return []
        # problem is that If we don't do bottom up then we need to
        # maintain lots of parent back and forth pointers
        
        def get_forest(root):
            # base care
            if root is None:
                return None
            
            # recursively call on left 
            root.left = get_forest(root.left)
            # recursively call on right
            root.right = get_forest(root.right)
            
            # if current node is in delted set
            # we need to process and add it to forest
            # we can do it because we are doing bottom up and 
            # and all the nodes at bottom than current are already processed
            if root.val in deleted_set:
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)
                # we are removing that node so that parent points points to None 
                # and we already added child to forest
                return None
            # if current node is not to be deleted return it
            return root
        
        get_forest(root)
        if root.val not in deleted_set:
            forest.append(root)
        
        return forest
            
