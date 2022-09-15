"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals or len(intervals)==0:
            return []
        
        
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]
        for index, interval in enumerate(intervals[1:]):
            st = interval[0]
            end = interval[1]
            # merge
            
            if st <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append(interval)
                
        return result
