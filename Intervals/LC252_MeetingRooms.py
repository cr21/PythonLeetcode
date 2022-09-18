"""

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) <=1:
            return True
        
        
        h = []
        # sort interval 
        # because we wanted to make sure we can attend all meetings
        # if they are sorted it's easy to find if there are overlapping meeting
        # so we quickly returns
    
        intervals = sorted(intervals)
        
        prev = intervals[0]
        
        for interval in intervals[1:]:
            st = interval[0]
            end = interval[1]
            
            # if overlapping interval return False
            if prev[1]> st:
                return False
            prev = interval
            
        return True
        
        
