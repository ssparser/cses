class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # For undirected graph

    def print_graph(self):
        for i in range(self.n):
            print(f"Node {i}: {self.adj[i]}")

if __name__ == "__main__":
    # Example usage:
    g = Graph(5)  # Create a graph with 5 nodes
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 4)


    g.print_graph()