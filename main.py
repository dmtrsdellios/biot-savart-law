import numpy as np

from plot import calculate_3d_plot


def main():
    phi = np.linspace(0, 2 * np.pi, 100)
    calculate_3d_plot(phi)


if __name__ == '__main__':
    main()
