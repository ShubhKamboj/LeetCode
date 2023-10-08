class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        string_check='{','}','(',')'
        for c in s:
            if c=='{' or  c =='[' or c == '(':
                stack.append(c)
            elif c =='}' or c ==']' or c ==')':
                if not stack:
                    return False
                elif (c==")" and stack[-1] =='(') or  (c=="}" and stack[-1] =='{') or (c=="]" and stack[-1] =='[') :
                   stack.pop()
                else:
                    return False
        
        return True if not stack else False
