"""

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        
        n,operand = 0,0
        
        def evalute_expression(stack):
        
            if not stack or type(stack[-1])==str:
                stack.append(0)
            
            res = stack.pop()
            
            while stack and stack[-1]!=')':
                sign = stack.pop()
                if sign=='+':
                    res+=stack.pop()
                else:
                    res-=stack.pop()
                    
            return res
        
        
        
        for index in range(len(s)-1,-1,-1):
            char = s[index]
            
            if char.isdigit():
                operand = (10**n*int(char))+operand
                n+=1
                
            elif char !=" ":
                
                if n:
                    stack.append(operand)
                    n, operand = 0,0
                    
                if char == '(':
                    res = evalute_expression(stack)
                    stack.pop()
                    stack.append(res)
                    
                else:
                    stack.append(char)
                
        if n:
            stack.append(operand)
        
        
        return evalute_expression(stack)
                    
                
            
            
        
