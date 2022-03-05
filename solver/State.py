class State:
    def __init__(self, name):
        self.name = name

    def __eq__(self, state):
        return self.name == state.name

    def __str__(self):
        return "<State [%s]>" % (self.name,)
