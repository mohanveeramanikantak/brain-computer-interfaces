# Brain Signal Simulation

import numpy as np
import matplotlib.pyplot as plt

# Generate fake EEG signal
time = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 10 * time) + np.random.normal(0, 0.5, 500)

# Plot
plt.plot(time, signal)
plt.title("Simulated EEG Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
