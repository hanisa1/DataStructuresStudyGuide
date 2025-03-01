class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            return "Queue is Full"
        elif self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            return "Queue is Empty"
        data = self.queue[self.front]
        if self.front == self.rear:  # Last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

# Example Usage
circularQueue = CircularQueue(5)
circularQueue.enqueue(10)
circularQueue.enqueue(20)
circularQueue.enqueue(30)
circularQueue.enqueue(40)
circularQueue.display()
print("Dequeued:", circularQueue.dequeue())
circularQueue.display()