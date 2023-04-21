import numpy as np
from scipy.integrate import quad
import sympy as smp


def calculate_magnetic_field(xv, yv, zv):
    t, x, y, z = smp.symbols('t, x, y, z')

    l = (1 + (3 / 4) * smp.sin(3 * t)) * smp.Matrix([smp.cos(t), smp.sin(t), 0])
    # l = smp.Matrix([smp.cos(t), smp.sin(t), (t-smp.pi)/smp.pi])
    r = smp.Matrix([x, y, z])
    sep = r - l

    integrand = smp.diff(l, t).cross(sep) / sep.norm() ** 3

    dBxdt = smp.lambdify([t, x, y, z], integrand[0])
    dBydt = smp.lambdify([t, x, y, z], integrand[1])
    dBzdt = smp.lambdify([t, x, y, z], integrand[2])

    return np.array([quad(dBxdt, 0, 2 * np.pi, args=(xv, yv, zv))[0],
                     quad(dBydt, 0, 2 * np.pi, args=(xv, yv, zv))[0],
                     quad(dBzdt, 0, 2 * np.pi, args=(xv, yv, zv))[0]])
