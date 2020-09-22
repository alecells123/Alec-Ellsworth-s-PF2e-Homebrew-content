class Handler:
    state = ""

    def __init__(self):
        self.state = "combat"

    def get_state(self):
        return self.state

    def    set_state(self, state):
        self.state = state

