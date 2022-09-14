"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

"""

class Solution(object):
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # first base case when intervals is empty
        if intervals is None or len(intervals)==0 :
            return [newInterval]
        intervals.sort(key = lambda x:x[0])
        
        res = []
        index = 0
        
        # find the location of the index start newInterval
        for i in range(index, len(intervals)):
            index=i
            st = intervals[i][0]
            if st > newInterval[0]:
                break
            res.append(intervals[i])
            
    
        # BASE case wherre we need to add newinterval at starts
        # check If we need to merge with new interval or not 
        if len(res) == 0:
            res.append(newInterval)
        else:
            # check if newInterval needs to be overlapped with previous one or not
            if(newInterval[0] <= res[-1][1]):
                res[-1][1] = max(newInterval[1], res[-1][1])
            else:
                res.append(newInterval)
        
        # now merge with other intervals
        for i in range(index, len(intervals)):
            st = intervals[i][0]
            en = intervals[i][1]
            # // overlapping
            if st <= res[-1][1]:
                res[-1][1] = max(en, res[-1][1])
            else:
                res.append(intervals[i])
        
        return res
                
        
