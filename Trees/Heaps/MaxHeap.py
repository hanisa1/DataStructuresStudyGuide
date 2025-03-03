import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)  # Negate values to simulate max heap

    def pop(self):
        return -heapq.heappop(self.heap)

# Example Usage
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(20)
max_heap.push(15)
print(max_heap.pop())  # Output: 20