"""

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

Find the minimum number of intervals after which the prices of a stock will increase

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # TLE O(N^2)
#         res = [0 for _ in range(len(temperatures))]
        
#         for day in range(len(temperatures)):
#             for future in range(day+1, len(temperatures)):
#                 if temperatures[future] > temperatures[day]:
#                     res[day] = future-day
#                     break
#         return res
                
        n = len(temperatures)
        res = [0]*n
        # add temprature and index in stack
        stack=[] # pair [temprature, index]
        for i, t in enumerate(temperatures):
            # while stack is not empty or current element
            # is greater than top of the stack
            # pop element from stack
            # update corosponding index
            while stack and t > stack[-1][0]:
                temp, id = stack.pop()     
                res[id] = i - id
            # if current temprature is less than top of the stack, push
            # it to stack
            # stack will always have monotonically decreasing temprature
            stack.append([t,i])
                
        return res
            

