from State import State

class ZeroHeuristic:
    def __init__(self, states, goal_state=None):
        # Zero Heuristic for Dijkstra
        self.zero_heuristic = {}
        for key in states:
            self.zero_heuristic[key] = 0
        self.goal_state = goal_state

    def set_goal_state(self, goal_state):
        self.goal_state = goal_state
    
    def compute(self, state: State) -> float:
        if not self.goal_state:
            print("Error: goal state not specified in heuristic object!")
            exit(-1)
        return 0
    
    def __getitem__(self, item):
        return self.zero_heuristic[item]

class GoalCountHeuristic:
    def __init__(self, goal_state=None):
        self.goal_count_heuristic = {}
        self.goal_state = goal_state

    def set_goal_state(self, goal_state):
        self.goal_state = goal_state
    
    def compute(self, state: State) -> float:
        if not self.goal_state:
            print("Error: goal state not specified in heuristic object!")
            exit(-1)
        broken_down_states = self.goal_state.name.split('|')
        count = 0
        for s in broken_down_states:
            if not s in state.name:
                count += 1
        self.goal_count_heuristic[state.name] = count
        return count
    
    def __getitem__(self, item):
        return self.goal_count_heuristic[item]