"""

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        
        
        points_dict = {(p[0],p[1]) for p in points}
    
        min_area=float("inf")
        # Iterate over every point which can be treated as Top Left (x1,y1) and Bottom Right (x2,y2) coordinate
        # and check if corosponding required coordinate to form rectangle (x1,y2) and (x2,y1)
        # if they are present in set then we found it
        # we could have sorted dictionary based on x coordinate
        for (x1,y1) in points_dict:
            for (x2, y2) in points_dict:
                if x1 > x2 and y1> y2:
                    
                    if (x2,y1) in points_dict and (x1,y2) in points_dict:
                        min_area = min(min_area,abs(y2-y1) * abs(x2-x1))
                        print(min_area)
        
        return 0 if min_area == float("inf") else min_area
