from State import State
from Action import Action
from typing import Dict

class Node:
    def __init__(self, state: State, g_cost: int, 
                is_closed: bool, is_open: bool, heuristic, action: Action, parent=None):
        self.state = state
        self.parent = parent
        self.is_open = is_open
        self.is_closed = is_closed

        self.action = action
        self.g_cost = g_cost
        self.heuristic = heuristic
        self.h_cost = heuristic.compute(state)
        self.f_cost = self.g_cost + self.h_cost

    def __lt__(self, other) -> bool:
        return self.f_cost <= other.f_cost
    
    def __str__(self):
        return ("<Node [%s] | \
                 [Closed: %r] | \
                 [Opened: %r] | \
                 [G_Cost: %.2f] | \
                 [H_Cost: %.2f] | \
                 [F_Cost: %.2f]>" % (
                     self.state.name,
                     self.is_closed,
                     self.is_open,
                     self.g_cost,
                     self.h_cost,
                     self.f_cost
                 )
        )
