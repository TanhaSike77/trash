stack = []

stack.append("A")
stack.append("B")
stack.append("C")
print("Stack :", stack)

topElement = stack[-2]
print("peek : ", topElement)

poppedElement = stack.pop()
print("Popped element : ", poppedElement)
print("Stack after pop :", stack)

isEmpty = not bool(stack)
print("Stack is empty :", isEmpty)
print("size of stack :", len(stack))