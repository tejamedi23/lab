import math

# Alpha-Beta Pruning function
def alpha_beta_pruning(depth, node_index, is_maximizer, values, alpha, beta):
    if depth == 3: # Leaf node reached (example: depth = 3)
        return values[node_index]
    if is_maximizer:
        max_eval = -math.inf
        for i in range(2): # Each node has 2 children
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: # Pruning
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: # Pruning
                break
        return min_eval

# Example game tree (depth=3)
values = [3, 5, 6, 9, 1, 2, 0, -1] # Leaf nodes (Terminal values)
# Root node: depth=0, node_index=0, is_maximizer=True
optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
print(f"Optimal Value: {optimal_value}")
