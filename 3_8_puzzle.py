from collections import deque

# Function to print the puzzle state
def print_puzzle(state):
    for row in state:
        print(" ".join(str(cell) for cell in row))
    print("\n")

# Function to find the position of the empty tile (0)
def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j # Return row and column index

# Function to check if the puzzle is in the goal state
def is_goal(state, goal):
    return state == goal

# Function to generate possible moves
def get_neighbors(state):
    neighbors = []
    row, col = find_empty_tile(state)
    # Possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Swap 0 with the new position to create a new state
            new_state = [list(row) for row in state]
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append(new_state)
    return neighbors

# BFS Algorithm to solve the 8-Puzzle
def bfs_solver(initial, goal):
    queue = deque([(initial, [])]) # Queue stores (current_state, path)
    visited = set()
    while queue:
        current_state, path = queue.popleft()
        # Check if the goal is reached
        if is_goal(current_state, goal):
            return path + [current_state] # Return final path
        state_tuple = tuple(tuple(row) for row in current_state) # Convert to tuple for hashing
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        # Expand neighbors
        for neighbor in get_neighbors(current_state):
            queue.append((neighbor, path + [current_state]))
    return None # No solution found

# Define the initial and goal state
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Solve the puzzle using BFS
solution_path = bfs_solver(initial_state, goal_state)

# Print solution steps
if solution_path:
    print("Solution found in", len(solution_path) - 1, "steps:\n")
    for step, state in enumerate(solution_path):
        print("Step", step, ":")
        print_puzzle(state)
else:
    print("No solution found.")
