"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""


# Approach 1 BFS : 
## BFS traversal using queue having all atlantic ocean location and then all pacific ocean location
## then get the final answer by intersectionof both reachable location

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if len(heights)==0 or len(heights[0])==0 :
            return []
            
        atlanticQueue = deque()
        pacificQueue =  deque()
        
        # first row is connected to pacific
        # last row is connected to atlantic
        # first column is connected to pacific
        # last column is connected to atlantic
         
        m = len(heights);
        n = len(heights[0])
       
        for i in range(0,n):
            # first row reachble from pacific
            pacificQueue.append((0,i))
            # last row reachable from atlantic
            atlanticQueue.append((m-1,i));
            
        for i in range(m):
            # first column reachable from pacific
            
            pacificQueue.append((i,0))
            # last column reachable from atlantic
            atlanticQueue.append((i,n-1))
            
        
        # [0,1] = EAST
        # [0,-1] = WEST
        # [1,0] = SOUTH
        # [-1,0] = NORTH
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def BFS(queue) :
            reachble = [[False]*n for i in range(m)]
            print(reachble)
            while queue:
                location = queue.popleft()
                row,col = location[0], location[1]
                reachble[row][col] = True
                
                for _dir in dirs:
                    newR = row + _dir[0]
                    newC = col + _dir[1]
                    
                    # if out of bound continue
                    if newR < 0 or newR >= m or newC < 0 or newC >= n :
                        continue
                        
                    
                    
                    # if visited continue
                    if reachble[newR][newC]:
                        continue;
                        
                    # if new height is smaller than current cell height 
                    # continue
                    if heights[newR][newC] < heights[row][col]:
                        continue;
                    
                    queue.append((newR,newC))
                    
            return reachble
        
        atlantic_reachble = BFS(atlanticQueue)
        pacific_reachble = BFS(pacificQueue)
        
        
        res = []
        
        for i in range(m):
            for j in range(n):
                if atlantic_reachble[i][j] and pacific_reachble[i][j]:
                    res.append([i,j])
                    
        return res
        
        
                    
                    
                
           
  ## Approach 2 DFS
  
  class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if len(heights)==0 or len(heights[0])==0 :
            return []
            
        atlanticQueue = set()
        pacificQueue =  set()
        
        # first row is connected to pacific
        # last row is connected to atlantic
        # first column is connected to pacific
        # last column is connected to atlantic
         
        m = len(heights);
        n = len(heights[0])
       
        for i in range(0,n):
            # first row reachble from pacific
            pacificQueue.add((0,i))
            # last row reachable from atlantic
            atlanticQueue.add((m-1,i));
            
        for i in range(m):
            # first column reachable from pacific
            
            pacificQueue.add((i,0))
            # last column reachable from atlantic
            atlanticQueue.add((i,n-1))
            
        
        # [0,1] = EAST
        # [0,-1] = WEST
        # [1,0] = SOUTH
        # [-1,0] = NORTH
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        res=set()
        
        
        # DFS throught all celll to get reachable lcoation for both pacific and atlantic ocean
        def DFS(row, col, reachable):
            reachable.add((row, col))
            for _dir in dirs:
                newR = row + _dir[0]
                newC = col + _dir[1]

                # if out of bound continue
                if newR < 0 or newR >= m or newC < 0 or newC >= n :
                    continue

                # if visited continue
                if (newR,newC) in reachable:
                    continue

                # if new height is smaller than current cell height 
                # continue
                if heights[newR][newC] < heights[row][col]:
                    continue;

                DFS(newR,newC,reachable)

        
        pacific_reachable = set()
        atlantic_reachable= set()
        
        for location in  pacificQueue:
            row, col = location[0], location[1]
            DFS(row,col, pacific_reachable)
            
        for location in  atlanticQueue:
            row, col = location[0], location[1]
            DFS(row,col, atlantic_reachable)
          
        
        return list(pacific_reachable.intersection(atlantic_reachable))
    
    
                
                
            
            
        
        
        
        
        
