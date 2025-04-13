class GeneralLFSR:
    def __init__(self, initial_state, taps):
        self.state = initial_state
        self.taps = taps

    def get_current_state(self):
        return self.state

    def set_taps(self, taps):
        self.taps = taps

    def next_bit(self):
        feedback = 0
        for tap in self.taps:
            feedback ^= int(self.state[tap])
        self.state = self.state[1:] + str(feedback)  # Shift and add feedback
        return feedback