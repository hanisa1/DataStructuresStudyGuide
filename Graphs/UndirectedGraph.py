class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Connection both ways

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example Usage
ug = UndirectedGraph()
ug.add_edge(1, 2)
ug.add_edge(2, 3)
ug.add_edge(3, 1)
ug.display()