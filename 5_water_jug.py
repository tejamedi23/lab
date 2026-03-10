from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set() # To track visited states
    queue = deque([(0, 0)]) # Start state (0, 0)
    
    while queue:
        state = queue.popleft()
        a, b = state
        
        # If we have reached the target
        if a == target or b == target:
            print(f"Solution found: {state}")
            return True
            
        # If state is already visited, skip
        if state in visited:
            continue
            
        visited.add(state)
        
        # Generate possible next states
        possible_states = set()
        possible_states.add((jug1, b)) #Fill Jug1
        possible_states.add((a, jug2)) # Fill Jug2
        possible_states.add((0, b)) # Empty Jug1
        possible_states.add((a, 0)) # Empty Jug2
        
        #Pour from Jug1 -> Jug2
        pour_to_jug2 = min(a, jug2 - b)
        possible_states.add((a - pour_to_jug2, b + pour_to_jug2))
        
        #Pourfrom Jug2 -> Jug1
        pour_to_jug1 = min(b, jug1 - a)
        possible_states.add((a + pour_to_jug1, b - pour_to_jug1))
        
        # Add new states to queue
        for new_state in possible_states:
            if new_state not in visited:
                queue.append(new_state)
                
    print("No solution found.")
    return False

# Example Usage:
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
