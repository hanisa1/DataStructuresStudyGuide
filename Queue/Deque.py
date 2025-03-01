from collections import deque

class DequeQueue:
    def __init__(self):
        self.deque = deque()

    def add_front(self, item):
        self.deque.appendleft(item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.popleft()
        return "Deque is empty"

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        return "Deque is empty"

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

    def display(self):
        print("Deque:", list(self.deque))

# Example Usage
deque = DequeQueue()
deque.add_front(1)
deque.add_rear(2)
deque.add_front(0)
deque.display()
print("Removed from front:", deque.remove_front())
print("Removed from rear:", deque.remove_rear())
deque.display()