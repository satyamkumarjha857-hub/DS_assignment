graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

# Print the graph
print ("Adjacency List Representation:")
for vertex, neighbors in graph.items():
    print(vertex, "->", neighbors)

vertex = ["A", "B", "C", "D"]

matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0],  # D
]

print("\nAdjacency Matrix Representation:")
for row in matrix:
    print(row)  