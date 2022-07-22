"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if list1 is null return list2
        if not list1:
            return list2
        # if list2 is null return list1
        if not list2:
            return list1
        # current pointer will be used to move back and forth from list1 and list2 to maintain minimum sorting 
        curr = ListNode(-1)
        dummy = ListNode(-1,curr)
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
            
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
            
        return dummy.next.next
            
            
        
        
        
        
