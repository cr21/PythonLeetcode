"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n = len(s)
        segments=[]
        output=[]
        
        # check if segment part is valid or not 
        def valid(segment):
            
            # if length of segment is greater than 3 it is not valid
            # e.g 2555 is not valid segment
            if len(segment)>3:
                return False
            
            # checking make sure if first element is 0 it length should be only 1 else invalid
            return int(segment) <= 255  if segment[0]!='0' else len(segment)==1
        
        def update_output(cur_pos):
            # if all the dots are placed then check if last segment is valid or not
            # if it is valid add to result
            
            last_segment = s[cur_pos+1:n]
            print(last_segment)
            # checking if last segment is valid or not
            if valid(last_segment):
                # add last segment to currently formed segments
                segments.append(last_segment)
                # add final ip address to result list
                output.append(".".join(segments))
                # remove last added segment as a part of backtracking and moving
                segments.pop()
        
        # backtracking function
        # initially no dots are place so dots are 3 and starting index is -1
        def dfs(prev_pos=-1, dots=3):
            
            # maximum length of segment is 3 so we are iterative over maximum range of 3
            for cur_pos in range(prev_pos+1,min(n-1,prev_pos+4)):
                
                # current segment [prev_pos + 1 upto cur_pos]
                segment = s[prev_pos+1: cur_pos+1]
                
                # if selected current sagment is valid 
                if valid(segment):
                    segments.append(segment)
                    # found all the segments
                    if dots-1==0:
                        update_output(cur_pos)
                    else:
                        # recusrsion 
                        dfs(cur_pos, dots-1)
                    # remove the last added segment
                    # backtrack
                    segments.pop()
                    
        dfs() 
        return output
