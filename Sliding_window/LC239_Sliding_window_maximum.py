"""

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        deq = deque()
        
        output = []
        
        left = 0
        
        right = 0
        n = len(nums)
        while right < n :
            
            # nums = [1,3,-1,-3,5,3,6,7], k = 3
            # if element at current index is greater than top element of deque
            # keep on removing element from deque till element at right most position is greater or equal to current
            # element
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            # append current element to queue
            deq.append(right)
            
            # remove left from window
            
            if left > deq[0]:
                deq.popleft()
                
            # if we formed window of size k
            if (right + 1) >=k:
                output.append(nums[deq[0]])
                left+=1
                
            right+=1
                
        return output
            
            
            
            
            
        
        
