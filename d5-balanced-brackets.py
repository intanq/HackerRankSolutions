def isBalanced(s):
    # Write your code here
    open_brackets = ["[","(","{"]
    close_brackets= ["]",")","}"]
    stack = []
    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            if len(stack)>0 and open_brackets[close_brackets.index(i)] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
