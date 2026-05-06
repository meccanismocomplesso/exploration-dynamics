import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.simulation import run_simulation

positions, agent_types = run_simulation()

np.save(ROOT / "positions.npy", positions)
np.save(ROOT / "agent_types.npy", agent_types)

print("Simulation complete")