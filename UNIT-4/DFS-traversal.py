# DFS using recursion
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")   # Process the node
        visited.add(node)
        
        # Visit all neighbors
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Recursive Traversal starting from A:")
dfs_recursive(graph, 'A')
