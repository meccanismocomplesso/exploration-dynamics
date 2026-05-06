import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.metrics import coverage, entropy

positions = np.load(ROOT / "positions.npy")
agent_types = np.load(ROOT / "agent_types.npy")

cov = coverage(positions)
ent = entropy(positions)

print("Coverage:", cov)
print("Entropy:", ent)

figures_dir = ROOT / "figures"
figures_dir.mkdir(exist_ok=True)

final_positions = positions[-1]

embedded = final_positions[agent_types == "embedded"]
exploratory = final_positions[agent_types == "exploratory"]

plt.figure(figsize=(8,6))

plt.scatter(
    embedded[:,0],
    embedded[:,1],
    label="Embedded",
    alpha=0.7
)

plt.scatter(
    exploratory[:,0],
    exploratory[:,1],
    label="Exploratory",
    alpha=0.7
)

plt.legend()
plt.title("Embedded vs Exploratory Agents")
plt.savefig(figures_dir / "embedded_vs_exploratory.png")
plt.show()