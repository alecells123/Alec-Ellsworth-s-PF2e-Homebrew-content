class Handler:
    state = ""

    def __init__(self):
        self.state = "win_0"

    def get_state(self):
        return self.state

    def    set_state(self, state):
        self.state = state

