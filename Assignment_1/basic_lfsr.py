class BasicLFSR:
    def __init__(self, initial_state):
        self.state = initial_state

    def get_current_state(self):
        return self.state

    def next_bit(self):
        feedback = int(self.state[0]) ^ int(self.state[1])  # Example taps
        self.state = self.state[1:] + str(feedback)  # Shift and add feedback
        return feedback