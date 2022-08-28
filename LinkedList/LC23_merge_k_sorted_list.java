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
