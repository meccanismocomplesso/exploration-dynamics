import numpy as np
from .agents import Agent

def run_simulation(n_agents=50, p_exploratory=0.1, steps=200):
    agents = []
    center = np.array([0.0, 0.0])

    agent_types = []

    for _ in range(n_agents):
        if np.random.rand() < p_exploratory:
            agents.append(Agent(np.random.randn(2), "exploratory"))
            agent_types.append("exploratory")
        else:
            agents.append(Agent(np.random.randn(2), "embedded"))
            agent_types.append("embedded")

    positions = []

    for _ in range(steps):
        step_positions = []

        for agent in agents:
            agent.step(center=center)
            step_positions.append(agent.position.copy())

        positions.append(step_positions)

    return np.array(positions), np.array(agent_types)