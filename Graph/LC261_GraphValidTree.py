"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        build_graph = defaultdict(list)
        for edge in edges:
            s = edge[0]
            e =edge[1]
            build_graph[s].append(e)
            build_graph[e].append(s)
        
        
        visited = set()
        def dfs(root, parent):
            # if you ever found cycle it can not form Tree
            if root in visited:
                return False
            
            # mark visited
            visited.add(root)
            
            # iterate over every neighbour and run dfs
            for neigh in build_graph[root]:
                # to avoid edge that is leading to parent itself
                if neigh == parent:
                    continue
                # if children dfs return false there is cycle in graph return False
                if not dfs(neigh, root):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visited)
            
            
        
            
            
            
