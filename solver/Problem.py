from State import *

class Problem:
    def __init__(self, init: State, goal: State):
        self.init_state = init
        self.goal_state = goal

    def __str__(self):
        return ("<Problem [%s] | [%s]>" % (self.init_state, self.goal_state))