"""

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # APPROACH 3
        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        def squared_distance(point: List[int]) -> int:
            """Calculate and return the squared Euclidean distance."""
            return point[0] ** 2 + point[1] ** 2
        
        heap = [(-squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))

        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]
    
        
        
        # APPROACH 1
#         def get_distance(point):
#             return math.sqrt(point[0]**2+point[1]**2)
        
#         points.sort(key=get_distance)
#         return points[:k]

            # APPROACH 2
#         orders = defaultdict(list)
#         for point in points:
#             orders[get_distance(point)].append(point)
        
#         orders_sorted = sorted(dict(orders).items(), key = lambda x:x[0])
        
#         res =[]
        
#         for distances in orders_sorted:
#             res.extend(distances[1])
        
#         return res[:k]
        
  
  
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])
        
        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
