"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        # get Kth element in current group
        def getKth(curr, k):
            
            while curr and k>0:
                curr = curr.next
                k-=1
                
            return curr
        
        
        while True:
            kth = getKth(groupPrev, k)    
            # if Kth is None that means we reach to the. end of list and current group doest not have 
            # k element so we don't need to reverse it 
            # now get out of the loop by breaking
            if not kth:
                break
            
            # this will be start of next group
            groupNext = kth.next
            
            # reverse current group
            # prev node eventually points to head of the next group
            prev, curr = kth.next, groupPrev.next
            
            
            # reverse it
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # groupprev next will be end of the reverse operation
            # and that will be the node which will points to the reversal of next group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
            
        return dummy.next
        
        
