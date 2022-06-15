"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
Accepted
754.8K
Submissions

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rs = len(matrix)
        cs = len(matrix[0])
        
        k = rs*cs
            
        top = 0
        bottom = rs-1
        left = 0
        right = cs-1
        res = []
        while left <=right and top<=bottom:
            
            # row From top row till right column
            # LEFT to Right  top side
            for i in range(left, right+1):
                res.append(matrix[top][i])
            
            # Top to bottom (from right side)
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            
            # from right to left Bottom side
            if top != bottom:
                for i in range(right-1, left-1,-1):
                    res.append(matrix[bottom][i])
            
            # from bottom to top left side
            if left != right:
                for i in range(bottom-1, top,-1):
                    res.append(matrix[i][left])
                    
            left+=1
            right-=1
            top+=1
            bottom-=1
        return res
            
            
