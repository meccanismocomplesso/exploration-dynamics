import numpy as np

class Agent:
    def __init__(self, position, agent_type="embedded"):
        self.position = np.array(position, dtype=float)
        self.type = agent_type

    def step(self, center=None, noise=0.1):
        if self.type == "embedded":
            direction = center - self.position
            self.position += 0.1 * direction + np.random.uniform(-noise, noise, size=2)
        else:
            self.position += np.random.uniform(-noise, noise, size=2)
