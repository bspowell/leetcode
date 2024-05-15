def isValid(s):
    stack = []

    if len(s) < 2:
        return False
        
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')' or s[i] == ']' or s[i] == '}':
            if stack[-1] == '(' and s[i] == ')':
                stack.pop(-1)
            elif stack[-1] == '{' and s[i] == '}':
                stack.pop(-1)
            elif stack[-1] == '[' and s[i] == ']':
                stack.pop(-1)
            else:
                return False
    return True
    


print(isValid('()'))
print(isValid("()[]{}"))
print(isValid('(]'))
print(isValid('()'))
