from typing import Dict
from Action import *
from State import *

class TransitionMatrix:
    def __init__(self, actions: Dict, states: Dict):
        self.__actions = actions
        self.__states = states
        self.__mat = dict()

        # Generate a transition matrix (or adjacency matrix) 
        # All states are binded to their output states using a specific action and having a specific cost
        for state_name, state in self.__states.items():
            self.__mat[state_name] = []
            for _, action in self.__actions.items():
                if action.state_start == state:
                    if action.state_end.name not in states:
                        print("Warning: [%s] not in the provided list of states: \n[%s]" % (str(action.state_end.name), str(states)))
                    self.__mat[state_name].append((action, action.state_end, action.time))
        
    def __getitem__(self, item):
        return self.__mat[item]

    def __str__(self):
        return str(self.__mat)