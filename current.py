import numpy as np


# Calculate current density
def calculate_current(phi):
    return (1 + 3 / 4 * np.sin(3 * phi)) * np.array([np.cos(phi), np.sin(phi), np.zeros(len(phi))])
