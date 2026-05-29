from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft() if self.queue else None

    def top(self):
        return self.queue[0] if self.queue else None

    def empty(self):
        return len(self.queue) == 0

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())   
print(myStack.pop())   
print(myStack.empty()) 