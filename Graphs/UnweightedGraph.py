class UnweightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example Usage
ug = UnweightedGraph()
ug.add_edge(1, 2)
ug.add_edge(2, 3)
ug.add_edge(3, 1)
ug.display()