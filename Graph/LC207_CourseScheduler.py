

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree=[0]*numCourses
        # build Graph and indegree vector
        for id,preq in enumerate(prerequisites):
            graph[preq[1]].append(preq[0])
            indegree[preq[0]]+=1
            
        q = []
        
        # all the nodes which does not have any indegree we can start them any order
        # without prerequisites so add it to queue
        for index,degree in enumerate(indegree):
            if degree==0:
                q.append(index)
                
        while q:
            # popped out node from queue
            node = q.pop()
            neighs = graph.get(node)
            # now we have finish prerequsite course
            # so remove it from it's dependent ( decrease indegree count)
            if neighs:
                for neigh in neighs:
                    # reduce indegree
                    indegree[neigh]-=1
                    # when indegree becomes zero add it to queue
                    if indegree[neigh]==0:
                        q.append(neigh)
        
        
        for degree in indegree:
            if(degree>0):
                return False
        
        return True
                        
                
            
