class MonkeyBananaProblem:
    def __init__(self):
        self.initial_state = ("floor", "chair_far", "monkey_far", "bananas_hanging") # Initial positions
        self.goal_state = ("on_chair", "chair_under_banana", "monkey_near", "bananas_got") #Goal state
        
    def actions(self, state):
        # Returns possible actions for a given state
        possible_actions = []
        monkey, chair, monkey_pos, banana = state
        if monkey_pos == "monkey_far":
            possible_actions.append("move_near_chair") # Move towards the chair
        if monkey == "floor" and monkey_pos== "monkey_near":
            possible_actions.append("push_chair_under_banana")
        if monkey =="floor" and chair == "chair_under_banana":
            #Move chair under bananas
            possible_actions.append("climb_chair") # Climb onto chair
        if monkey == "on_chair" and chair == "chair_under_banana":
            possible_actions.append("grab_bananas") # Grab bananas
        return possible_actions
        
    def result(self, state, action):
        # Returns the new state after performing an action.
        monkey, chair, monkey_pos, banana = state
        if action == "move_near_chair":
            return ("floor", "chair_far", "monkey_near", banana)
        if action == "push_chair_under_banana":
            return ("floor", "chair_under_banana", "monkey_near", banana)
        if action == "climb_chair":
            return ("on_chair", "chair_under_banana", "monkey_near", banana)
        if action =="grab_bananas":
            return ("on_chair", "chair_under_banana", "monkey_near", "bananas_got")
        return state
        
    def solve(self):
        # Performs a Depth-First Search (DFS) to reach the goal state
        stack = [(self.initial_state, [])] # (state, path)
        visited = set()
        while stack:
            state, path = stack.pop()
            if state == self.goal_state:
                return path + ["Success: Monkey has bananas!"]
            if state not in visited:
                visited.add(state)
                for action in self.actions(state):
                    new_state = self.result(state, action)
                    stack.append((new_state, path + [action]))
        return "No solution found."

#Solve the problem
problem = MonkeyBananaProblem()
solution = problem.solve()

# Print the solution steps
if isinstance(solution, list):
    for step in solution:
        print(step)
else:
    print(solution)
