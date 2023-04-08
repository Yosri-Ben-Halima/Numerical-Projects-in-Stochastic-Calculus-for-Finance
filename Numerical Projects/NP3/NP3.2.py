import numpy as np
import matplotlib.pyplot as plt

# Set parameters
rate = 1
t_start = 0
t_end = 10
step_size = 0.01
num_paths = 10

# Generate time points
time_points = np.arange(t_start, t_end+step_size, step_size)

# Generate and plot Poisson process paths

# Generate all random counts for all paths and all time steps
counts = np.random.poisson(rate * step_size, size=(num_paths, len(time_points)-1))

# Compute the cumulative sum along the time axis
cumulative_counts = np.cumsum(counts, axis=1)

# Add a column of zeros at the beginning of each path to represent the initial count (0)
paths = np.column_stack((np.zeros(num_paths), cumulative_counts))

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(8,5))

# Plot Poisson process paths on the subplot
for i in range(num_paths):
    ax.plot(time_points, paths[i], label=f"Path {i+1}")

ax.set_title(f"{num_paths} Poisson Process Paths (Rate = {rate})")
ax.set_xlabel("Time")
ax.set_ylabel("Count")
ax.legend()

# Display the final plot
plt.show()
