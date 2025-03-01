class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)

# Example Usage
simpleQueue = SimpleQueue()
simpleQueue.enqueue(1)
simpleQueue.enqueue(2)
simpleQueue.enqueue(3)
simpleQueue.display()
print("Dequeued:", simpleQueue.dequeue())
simpleQueue.display()