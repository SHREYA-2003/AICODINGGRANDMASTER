import numpy as np
import matplotlib.pyplot as plt

# Generate non-normal data (uniform distribution)
data = np.random.uniform(0, 1, 10000)

sample_means = []

# Take samples and compute means
for _ in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))

# Plot histogram
plt.hist(sample_means, bins=30)
plt.title("Central Limit Theorem Demonstration")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
