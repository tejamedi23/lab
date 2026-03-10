from itertools import permutations

# Brute Force Approach
def tsp_brute_force(graph, start=0):
    cities = list(range(len(graph))) # Cities index
    cities.remove(start) # Start from first city
    min_path = float("inf")
    best_route = None
    for perm in permutations(cities): # Try all possible routes
        route = [start] + list(perm) + [start] # Add start & end city
        cost = sum(graph[route[i]][route[i + 1]] for i in range(len(route) - 1))
        if cost < min_path:
            min_path = cost
            best_route = route
    return best_route, min_path
    
# Example Graph (Distance Matrix)
graph =[
    [0, 10, 15, 20], # City 0
    [10, 0, 35, 25], # City 1
    [15, 35, 0, 30], # City 2
    [20, 25, 30, 0] # City 3
]

# Solve TSP
route, cost = tsp_brute_force(graph)
print(f"Optimal Route: {route}, Minimum Cost: {cost}")
