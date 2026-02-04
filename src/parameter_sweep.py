import numpy as np
import matplotlib.pyplot as plt
from realism_metric import realism_error

time = np.linspace(0, 1, 200)
measured = 10 * np.sin(2 * np.pi * time)

phase_offsets = np.linspace(0, 0.5, 25)
errors = []

for phase in phase_offsets:
    simulated = 10 * np.sin(2 * np.pi * time + phase)
    errors.append(realism_error(simulated, measured))

plt.plot(phase_offsets, errors, marker='o')
plt.xlabel("Phase Offset (rad)")
plt.ylabel("Normalized Realism Error")
plt.title("Sensitivity of Realism Error to Contact Phase")
plt.grid(True)
plt.tight_layout()
plt.show()
