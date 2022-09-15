"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Approach 2 Fast and Slow Pointer
        dummy = ListNode(0)
        dummy.next= head
        slow = dummy
        
        fast = dummy
        
        for index in range(0,n+1):
            fast = fast.next
            
        while fast!=None : 
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
    
        # Approach 1 : Find Length
        
        def find_length(head):
            node = head
            len = 0
            while node:
                len+=1
                node=node.next
            return len
        len = find_length(head)
        
        k = len - n
        
        
        node = head
        
        ## base case:
        if k == 0:
            return head.next
        else:
            
            while (k-1) > 0:
                node = node.next
                k-=1

            node.next = node.next.next

            return head
                
            
