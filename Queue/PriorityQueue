import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def enqueue(self, item, priority):
        heapq.heappush(self.pq, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.pq)[1]  # Return item, not priority
        return "Priority Queue is empty"

    def is_empty(self):
        return len(self.pq) == 0

    def display(self):
        print("Priority Queue:", [item[1] for item in sorted(self.pq)])

# Example Usage
priorityQueue = PriorityQueue()
priorityQueue.enqueue("Task A", 3)
priorityQueue.enqueue("Task B", 1)
priorityQueue.enqueue("Task C", 2)
priorityQueue.display()
print("Dequeued:", priorityQueue.dequeue())
priorityQueue.display()