"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        # Appraoch 1 : TLE : 70/73 test cases passes
        # dp=[[0]*len(maxtrix[0]) for _ in range(len(matrix))]
        # dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
#         maxarea=0
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]=='0' : continue
#                 # compute the maximum width and update dp with it
#                 width = dp[i][j] = dp[i][j-1]+1 if j else 1
#                 # compute the maximum area rectangle with a lower right corner at [i, j]
#                 for k in range(i,-1,-1):
#                     width = min(width, dp[k][j])
#                     maxarea = max(maxarea, width * (i-k+1) )
                    
#         return maxarea
                
    
        # Approach 2 Largest histogram based approach
        
        
        
        if not matrix: return 0
    
        def largest_rectange_histogram(heights):
            max_area = 0
            stack = deque()
            stack.append(-1)

            for index in range(len(heights)):
                # pop out the element if current height is less than top of stack

                while (stack[-1] != -1 and heights[stack[-1]] >= heights[index] ):
                    current_height = heights[stack.pop()]
                    current_width = index - stack[-1]-1

                    max_area = max(max_area, current_width*current_height)
                stack.append(index)

            while stack[-1]!=-1:
                current_height = heights[stack.pop()]
                current_width = len(heights)-stack[-1]-1
                max_area = max(max_area, current_width*current_height)
            return max_area
        
        maxarea=0
        
        dp=[0]* len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                dp[j]= dp[j]+1 if matrix[i][j] == '1' else 0
            print(dp)
                
            maxarea = max(maxarea,largest_rectange_histogram(dp))
            
        return maxarea
        
