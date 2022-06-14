"""
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

Example 1:


Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
 

Constraints:

m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
"""

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m = len(mat1)
        n = len(mat1[0])
        
        res=[ [0]*len(mat2[0]) for _ in range(len(mat1))]
        
            
        # compress matrix will iterate over matrix 
        # and for each row only stores non zero value and corosponding column
        def compress_matrix(mat1):
            cm = [[] for _ in range(len(mat1))]
            
            for i in range(len(mat1)):
                
                for j in range(len(mat1[0])):
                    if mat1[i][j] != 0 :
                        cm[i].append((mat1[i][j], j))
            return cm
        
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        A = compress_matrix(mat1)
        B = compress_matrix(mat2)
        print(A)
        print(B)
            
        for mat1_row in range(m):
            # get all non zero column with current row
            for element1, mat1_column in A[mat1_row]:
                # get mat2_row from B and multiply
                # for each non zero column in mat1 row, find corosponding row in mat2 and 
                # get all the column element with nonzero values to multiply
                for element2, mat2_column in B[mat1_column]:
                    res[mat1_row][mat2_column] += element1*element2
                    
        return res
    
        
                   
            
