"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

"""

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        
        if(intervals == null || intervals.length == 0) return 0;
        
        if(intervals.length == 1) return 1;
        
        // sort based on start time
        Arrays.sort(intervals, (a,b) -> a[0]-b[0] ) ;
        // ((A,B) -> A-B);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> a-b);
        
    
        pq.add(intervals[0][1]);
        
        for(int index=1;index< intervals.length;index++) {
            int[] interval = intervals[index];
            int end = interval[1];
            int st = interval[0];
            
            int top = pq.poll();
            
            if ( st >=top){
               pq.add(end);
            }
            else{
                pq.add(top);
                pq.add(end);
            }
                
        }
        
        return pq.size();
        
    }
}
