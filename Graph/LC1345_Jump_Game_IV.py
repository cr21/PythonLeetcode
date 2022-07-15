"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108

"""

# APPROACH 1 :  BFS :


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        if len(arr)<=1:
            return 0
        
        k = len(arr)
        graph = {}
        # group the same value nodes togather and store their indexes
        # this bookeeping will help 
        for index in range(k):
            if arr[index] in graph:
                graph[arr[index]].append(index)
            else:
                graph[arr[index]]=[index]
                
        
        
        current= [0]
        visited={0}
        steps=0
        
        # while current has some node to processed
        while current:
            next_nodes=[]
            
            # process current layer
            for node in current:
                # if we ever reached the last index return
                if node == k-1:
                    return steps
                
                # check for same value and add it to the next_layers process set
                # because apart from the next and prev index neigh we will process
                # same value index as well
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        next_nodes.append(child)
                
                # process the node remove from graph to avoid redudant search
                # MOST IMPORTANT IF YOU COMMENT IT TLE for some cases
                # we don't want to process once it is added to next_nodes
                graph[arr[node]].clear()
                
                # not check for neighbors for processing 
                for child in [node-1, node+1]:
                    if child >=0 and child < k and child not in visited:
                        visited.add(child)
                        next_nodes.append(child)
            # assign next layers to current for further processing
        
            current = next_nodes
            # increment steps
            steps+=1
                
                    
        
# APPROACH 2 : BIDirectional BFS



