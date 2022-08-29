"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

# we can only add Closed if Total Open > Total Closed


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        # A. We can only add Open if Total Open used < n
        # B.  we can only add Closed if Total Open > Total Closed
        # C.  We will stop when TotalClosed. == TotalOpendd == n
        
        res = []
        stack=[]
        def backtrack(openCount, closedCount):
            # C. We will stop when TotalClosed. == TotalOpendd == n
            if openCount == closedCount == n :
                res.append("".join(stack))
                return
            
            # A. We can only add Open if Total Open used < n
            if openCount < n:
                stack.append("(")
                backtrack(openCount+1,closedCount )
                stack.pop()
            # B. we can only add Closed if Total Open > Total Closed
            if openCount > closedCount:
                stack.append(")")
                backtrack(openCount,closedCount +1)
                stack.pop()
        backtrack(0,0)
        return res
