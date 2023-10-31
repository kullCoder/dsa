# Kruskal's algorithm in Python

# Define a class for a graph
class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the number of vertices
        self.V = vertices
        self.graph = []

    # Add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function to find the parent of a node
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Apply union operation to combine two sets
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Applying Kruskal's algorithm to find the MST
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        # Sort the graph edges by their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

# Create a graph with 6 vertices
g = Graph(6)

# Add edges to the graph
# (u, v, w) represents an edge from vertex u to vertex v with weight w
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
# Add more edges...

# Apply Kruskal's algorithm to find the Minimum Spanning Tree
g.kruskal_algo()
