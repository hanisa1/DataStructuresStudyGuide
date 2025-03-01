class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)

# Example Usage
sampleStack = Stack()
sampleStack.push(1)
sampleStack.push(2)
sampleStack.push(3)
sampleStack.display()
print("Popped:", sampleStack.pop())
print("Top element:", sampleStack.peek())
sampleStack.display()