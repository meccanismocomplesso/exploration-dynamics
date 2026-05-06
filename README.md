# Exploration Dynamics in Agent-Based Systems

This repository explores minimal exploration dynamics in agent-based systems,
focusing on the difference between random-walk exploration and locally constrained motion.

## Motivation

In many models, exploration is associated with optimization or goal-directed behavior.
Here we show that simple stochastic movement (random walk) is sufficient to produce
non-trivial spatial and dynamical structure.

## Model

We consider two types of agents:

- Embedded agents: locally constrained, biased toward a center
- Exploratory agents: random-walk dynamics

We compare:

- Random walk vs biased movement
- Spatial coverage
- Transition frequency

## Metrics

- Coverage (visited area)
- Entropy of positions
- Switching rate

## Run

```bash
pip install -r requirements.txt
python scripts/run_simulation.py
python scripts/analyze.py