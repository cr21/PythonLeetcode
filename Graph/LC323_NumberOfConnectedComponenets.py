"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        total_components = 0
        
        visited=set()
        
        def buildGraph(n, edges):
            graph = {index:[] for index in range(n)}
            
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
                
            return graph
        
        
        def dfs(node, parent):
            # mark node
            visited.add(node)
            
            neighList = graph.get(node)
            if not neighList or len(neighList)==0:
                return
            
            for neigh in neighList:
                # for back edges leads to parent and check if neigh is not
                # visited by some other DFS action
                if neigh != parent and neigh not in visited:
                    dfs(neigh, node)
                    
        
        
        
        graph = buildGraph(n, edges)
        
        
        # for each of the node run dfs if it is not already visisted
        for index in range(n):
            if index not in visited:
                dfs(index, -1)
                total_components+=1
                
                
        return total_components
