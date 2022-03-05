from State import *
from typing import List

class Action:
    def __init__(self, name: str, state_start: State, state_end: State,
                 time: int):
        self.name = name
        self.state_start = state_start
        self.state_end = state_end
        self.time = time
    
    def get_children(self, input_state: State, states: List[State]) -> List[State]:
        pass
