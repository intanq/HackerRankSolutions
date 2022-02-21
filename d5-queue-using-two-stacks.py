def enqueue (element, stack1):
    stack1.append(element)

def dequeue (stack1,stack2):
    if len(stack2) == 0:
        while len(stack1) != 0:
            stack2.append(stack1.pop())
    if len(stack2) != 0:
        stack2.pop()

def printElement (stack1,stack2):
    if len(stack2) == 0:
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        print(stack2[-1])
    else:
        print(stack2[-1])
