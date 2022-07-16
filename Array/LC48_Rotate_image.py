"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        """
        def transpose(matrix):
            
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix[0])):
                    
                    matrix[i][j], matrix[j][i]  =  matrix[j][i] , matrix[i][j]
                    
        
        
        def reverse(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])//2):
                    
                    matrix[i][j], matrix[i][-j-1]  = matrix[i][-j-1],   matrix[i][j]
        
            
        # print(matrix)
        transpose(matrix)
        reverse(matrix)
        return matrix
        
#         left = 0
#         right = len(matrix)-1
        
#         while left < right:
            
#             # for each iteration of outer circulation 
#             # right - left will move in space by 1. in each direction
            
#             for i in range(right-left):
#                 top = left
#                 bottom = right
#                 top_left = matrix[top][left+i]
                
#                 #  replace boomLeft to top left
#                 matrix[top][left+i] = matrix[bottom-i][left]
                
#                 # replace bottom right to bottom left
                
#                 matrix[bottom-i][left] = matrix[bottom][right-i]
                
#                 # replace top right to bottom right
                
#                 matrix[bottom][right-i] = matrix[top+i][right]
                
#                 matrix[top+i][right] = top_left
                
#             left+=1
#             right-=1
            
#         return matrix
