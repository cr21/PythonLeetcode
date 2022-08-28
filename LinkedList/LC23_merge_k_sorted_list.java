23. Merge k Sorted Lists

"""

  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

"""

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
        if(lists == null || lists.length == 0 ){
            return null;
        }
        
       
        PriorityQueue<ListNode> pq = new PriorityQueue<>(
            
            (ListNode a, ListNode b)->{ return a.val - b.val;}
        );
        
       
        for(ListNode list:lists){
            if (list !=null) pq.add(list);
            
        }
        
        
        ListNode dummy = new ListNode(-1);
        ListNode res = dummy;
        
        while (!pq.isEmpty()){
            ListNode node = pq.poll();
            ListNode next_node = node.next;
            
            if(next_node != null){
                pq.add(next_node);
            }
            
            
            
            dummy.next = node;
            dummy = dummy.next;
            
            
            
        }
        
        return res.next;
        
    }
}


### PYTHONN


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        if len(lists)==1:
            return lists[0]
        
        
        
        res = None
        index = 0
        
        
        
        def merge_2_list(list1, list2):
            
            
            if not list1:
                return list2
            
            if not list2:
                return list1


            cur = ListNode(-1)
            dummy = ListNode(-1, cur)


            while list1 and list2:

                if list1.val <= list2.val:
                    cur.next = list1
                    list1=list1.next
                    cur = cur.next
                elif list2.val <= list1.val:
                    cur.next = list2
                    list2=list2.next
                    cur = cur.next


            # if one of the list goes out of bound
            # iterate over next list

            while list1:
                cur.next = list1
                list1=list1.next
                cur = cur.next

            while list2:
                cur.next = list2
                list2=list2.next
                cur = cur.next

            return dummy.next.next
        
        
        
       
        
        while index < len(lists):
            
            list1 = lists[index]
            index = index+1
            if index <  len(lists):
                list2=lists[index]
                # we found two list
                # merge it first
                merged= merge_2_list(list1, list2)
                # merged response list with merge output from above
                res = merge_2_list(res,merged )
                index+=1
            else:
                # no matching pair found so merge with resultant merged 
                res = merge_2_list(res, list1)
            
            
        return res
        
        
        
