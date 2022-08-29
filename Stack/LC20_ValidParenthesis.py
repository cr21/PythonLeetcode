"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        
        
        stack = []
        
        left = 0
        
        for left in range(len(s)):
            
            ch = s[left]
            
            if  ch in ['(','{','[']:
                stack.append(ch)
            else:
                # if stack is empty and first char is closing bracker return False
                if len(stack) == 0 :
                    return False
                # MAtching pair found popped up
                if (ch == ']' and stack[-1] == '[') or ( ch == ')' and stack[-1] == '(') or ( ch == '}' and stack[-1] == '{') :
                    stack.pop()

                else:
                    stack.append(ch)
            
        return len(stack)==0
            
