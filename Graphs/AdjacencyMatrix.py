class AdjacencyMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1  # Add an edge

    def display(self):
        for row in self.matrix:
            print(row)

# Example Usage
am = AdjacencyMatrix(4)
am.add_edge(0, 1)
am.add_edge(1, 2)
am.add_edge(2, 3)
am.display()