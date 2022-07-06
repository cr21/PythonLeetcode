"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.

"""
# Approch 1 ITERATIVE

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        
        visited={}
        dummy = Node(-1,head)
        # print(dummy.next.val)
        
        
        def deepcopy(node):
            
            if node:
                # if node already created return it
                if node in visited:
                    return visited[node]
                else:
                  # create new Node and return it
                    visited[node]=Node(node.val, None,Node)
                    return visited[node]
            return None
        
        
        # deep copy of head node first
        
        old_head = head
        
        new_node = Node(old_head.val, None,None)
        # old_head is assigned with new_node
        visited[old_head]=new_node
        
        # keep on deep copying list till we don't have any next pointer
        while old_head:
            new_node.random = deepcopy(old_head.random)
            new_node.next= deepcopy(old_head.next)
            old_head  = old_head.next
            new_node = new_node.next
        
        return visited[head]
            
        
        
  ### RECURSIVE APPAROCH

  class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        
        self.visited={}
        
        def deepcopy( head):
            if not head:
                return None

            if head in self.visited:
                return self.visited[head]

            # deep copy new Node
            node = Node(head.val, None, None)

            # do not recursively create again, so bookeeping it
            self.visited[head]= node
            
            # recursively create next and random pointer
            node.next = deepcopy(head.next)
            node.random = deepcopy(head.random)

            return node
    
        return deepcopy(head)
        
