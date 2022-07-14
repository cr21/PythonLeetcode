"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

"""


class TimeMap:

    def __init__(self):
        self.tMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tMap:
            return ""
        
        candidates = self.tMap[key]
        # if time stamp is out of bound 
        if candidates and len(candidates)>=0:
            if timestamp < candidates[0][0]:
                return ""
            if timestamp > candidates[-1][0]:
                return candidates[-1][1]
        
        # if timestamp is within bound do binary search and return the value corosponding to timestamp value less or equals to the required time stamp
        
        
        def BS(arr, value):
            result =" "
            left = 0
            right = len(arr)-1
            
            while left <= right:
                mid = (left + right)//2
                mid_time = arr[mid][0]
                mid_value = arr[mid][1]
                if mid_time == value:
                    return mid_value
                
                elif mid_time < value:
                    # Either our value is located in right side of mid
                    # or if value is not present in right side of mid 
                    # then lowest value that is less than mid should be 
                    # result value
                    result = mid_value
                    left = mid+1
                else:
                    right = mid-1
            
            return result
        
        return BS(candidates, timestamp)
        
        # if you don't want to implement Binary search do this
        # index = bisect.bisect_right(candidates, timestamp, key=lambda x: x[0])
        # return candidates[index - 1][1] if index else ''

