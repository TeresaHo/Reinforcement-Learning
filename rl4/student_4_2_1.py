#!/usr/bin/env python3
# rewards: [golden_fish, jellyfish_1, jellyfish_2, ... , step]
rewards = [10, -10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10]

# Q learning learning rate
alpha = 0.7

# Q learning discount rate
gamma = 0.2

# Epsilon initial
epsilon_initial = 1

# Epsilon final
epsilon_final = 0.1

# Annealing timesteps
annealing_timesteps = 1000

# threshold
threshold = 1e-6
