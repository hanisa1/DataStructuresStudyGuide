class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example Usage
wg = WeightedGraph()
wg.add_edge(1, 2, 5)
wg.add_edge(2, 3, 10)
wg.add_edge(3, 1, 2)
wg.display()