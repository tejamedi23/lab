from collections import deque

# BFS function
def bfs(graph, start):
    visited = set() # To track visited nodes
    queue = deque([start]) # Initialize queue with the start node
    while queue:
        node = queue.popleft() # Remove and process the first node
        if node not in visited:
            print(node, end=" ") # Print or process the node
            visited.add(node) # Mark it as visited
            queue.extend(graph[node]) # Add neighbors to the queue

# Example graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Running BFS from node 'A'
print("BFS Traversal:")
bfs(graph, 'A')
print("\n")


# DFS function (Non-Recursive)
def dfs(graph, start):
    stack = [start] # Use stack for DFS
    visited = set() # Set to track visited nodes
    while stack:
        node = stack.pop() # Remove last element from stack
        if node not in visited:
            print(node, end=" ") # Process the node
            visited.add(node) # Mark as visited
            # Add neighbors to stack (in reverse order for correct order)
            stack.extend(reversed(graph[node]))

# Running DFS from node 'A'
print("DFS Traversal (Non-Recursive):")
dfs(graph, "A")
print()
