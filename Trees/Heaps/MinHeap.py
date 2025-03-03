import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)

# Example Usage
min_heap = MinHeap()
min_heap.push(10)
min_heap.push(20)
min_heap.push(5)
print(min_heap.pop())  # Output: 5