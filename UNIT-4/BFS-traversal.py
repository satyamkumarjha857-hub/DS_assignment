from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize queue with the starting node
    
    while queue:
        node = queue.popleft()   # Remove from front of queue
        if node not in visited:
            print(node, end=" ") # Process the node (here we just print it)
            visited.add(node)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from node 'A'
print("BFS Traversal starting from A:")
bfs(graph, 'A')
