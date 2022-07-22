"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # sample example 1->2->3->4->5
        dummy = ListNode(0, head)
        
        leftprev, curr = dummy, head
        
        #1) traverse until current pointer points to left, and prev pointer one before left
        # 1->2->3->4->5 Left = 2 
        # leftprev = 1
        # curr =2 
        for i in range(left-1):
            leftprev, curr = curr, curr.next
            
                
            
        # 2) now reverse linkedlist but stop when you encounter right pointer
        # reverse from left to right
        
        prev=None
        # 2->3->4->5  4 = right
        # curr = 5
        # prev = 4 right
        for i in range(right-left+1):
            temp = curr.next
            curr.next= prev
            prev = curr
            curr = temp
            
        ## 3) re arranging leftprev pointer point to head of reverse 
        # and next of left prev pointer to point to to curr.next
        # 2->5
        leftprev.next.next = curr # current is node after right
        # 1->4
        leftprev.next = prev # prev is the right node
        
        return dummy.next
            
        

    
