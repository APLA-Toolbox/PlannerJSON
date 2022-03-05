from typing import Dict
from Action import *
from State import *

class TransitionMatrix:
    def __init__(self, actions: Dict, states: Dict):
        self.__actions = actions
        self.__states = states
        self.mat = dict()

        for state_name, state in self.__states.items():
            self.mat[state_name] = []
            for _, action in self.__actions.items():
                if action.state_start == state and action.state_end.name in states:
                    self.mat[state_name].append((action, action.state_end, action.time))
        
    def __getitem__(self, item):
        return self.mat[item]

    def __str__(self):
        return str(self.mat)