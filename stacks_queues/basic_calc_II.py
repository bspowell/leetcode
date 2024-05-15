# Division, Multi, Addition, Subtraction

# remove whitespaces
# as we iterate over the string, if we run into a division or multi, we need to 
# undo the previous operation, and then conduct the new operation. Then redo the previous opp
def calculate(s):
    stack, num, sign = [], 0, '+'
    
    for i in range(len(s)):
        
        if s[i].isdigit():
            num = (num * 10) + int(s[i])
        if s[i] in '+-*/' or i == len(s) - 1:
            
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                stack.append(stack.pop() * num)
            if sign == '/':
                p = stack.pop()
                res = abs(p) // num
                stack.append(res if p >= 0 else -res)
            num = 0
            sign = s[i]
            
    return sum(stack)