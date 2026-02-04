import numpy as np
import matplotlib.pyplot as plt

def realism_error(simulated, measured):
    """
    Compute normalized realism error between simulation and real data.
    """
    simulated = np.asarray(simulated)
    measured = np.asarray(measured)

    error = np.linalg.norm(simulated - measured) / np.linalg.norm(measured)
    return error


if __name__ == "__main__":
    # Example: contact force over time
    time = np.linspace(0, 1, 100)

    measured_force = 10 * np.sin(2 * np.pi * time)
    simulated_force = 10 * np.sin(2 * np.pi * time + 0.15)  # phase error

    err = realism_error(simulated_force, measured_force)
    print(f"Realism error: {err:.3f}")

    plt.plot(time, measured_force, label="Measured", linewidth=2)
    plt.plot(time, simulated_force, "--", label="Simulated")
    plt.xlabel("Time (s)")
    plt.ylabel("Force (N)")
    plt.title("Simulation vs Measured Contact Force")
    plt.legend()
    plt.tight_layout()
    plt.show()

