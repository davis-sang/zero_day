from collections import deque
from stacks import Stack


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("Peek:", s.peek())  # Output: 3
print("Pop:", s.pop())   # Output: 3
print("Peek after pop:", s.peek())  # Output: 2

# Similar stack with deque
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print("mystack: ", myStack)
# deque(['a', 'b', 'c'])

myStack.pop()
print("mystack after pop: ", myStack)
# deque(['a', 'b'])



