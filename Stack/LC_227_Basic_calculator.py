"""

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.


"""

class Solution:
    def calculate(self, s: str) -> int:
        
        length = len(s)
        if length==0:
            return 0
        
        stack = []
        
        current_number=0
        # keep track of which operation to perform on current number
        # by default it will be addition
        operation = '+'
        
        index = 0
        
        while index < length:
            curr_char = s[index]
            
            if curr_char.isdigit():
                current_number = (current_number*10)+(ord(curr_char)-ord('0'))
            
            if not curr_char.isdigit() and not curr_char.isspace() or index==length-1:
                if operation =='-':
                    stack.append(-current_number)
                elif operation =='+':
                    stack.append(current_number)
                elif operation =='*':
                   
                    stack.append(stack.pop()*current_number)
                elif operation =='/':

                    stack.append(int(stack.pop()/current_number))
                operation = curr_char
                current_number = 0
                
            index+=1
            
            
        result = 0
        return sum(stack)
       
       
       ## APPROACH 2 no STACK
       
       length = len(s)
        if length==0:
            return 0
        
        last_number = 0
        result = 0
        
        current_number=0
        # keep track of which operation to perform on current number
        # by default it will be addition
        operation = '+'
        
        index = 0
        
        while index < length:
            curr_char = s[index]
            
            if curr_char.isdigit():
                current_number = (current_number*10)+(ord(curr_char)-ord('0'))
            
            if not curr_char.isdigit() and not curr_char.isspace() or index==length-1:
                if operation =='-' or  operation =='+':
                    result+=last_number
                    if (operation == '+'):
                        last_number = current_number   
                    else:
                        last_number = -current_number
                elif operation =='*':
                   
                    last_number = last_number * current_number
                elif operation =='/':

                    last_number = int(last_number / current_number)
                operation = curr_char
                current_number = 0
                
            index+=1
            
        result+=last_number
            
            
        return result
