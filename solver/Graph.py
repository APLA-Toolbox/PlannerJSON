from collections import deque
from TransitionMatrix import TransitionMatrix
from typing import Dict

class Graph:
    def __init__ (self, states: Dict, actions: Dict):
        self.transition_matrix = TransitionMatrix(actions, states)
        print(self.transition_matrix)
    
    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def heuristic(self, n):
        n = n
        return 0