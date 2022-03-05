from typing import Dict
from Action import *
from State import *

class TransitionMatrix:
    def __init__(self, actions: Dict, states: Dict):
        self.__actions = actions
        self.__states = states
        self.adjacency_list = dict()

        for state_name, state in self.__states:
            self.adjacency_list[state_name] = []
            for action_name, action in self.__actions:
                if action.state_start == state:
                    self.adjacency_list[state_name].append([action.state_end, action.time])
