import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from current import calculate_current
from magnetic_field import calculate_magnetic_field


def calculate_plot(phi):
    lx, ly, lz = calculate_current(phi)

    plt.figure(figsize=(7, 7))
    plt.plot(lx, ly)
    plt.xlabel('$x/R$', fontsize=25)
    plt.ylabel('$y/R$', fontsize=25)
    plt.show()


def calculate_3d_plot(phi):
    lx, ly, lz = calculate_current(phi)
    x = np.linspace(-2, 2, 20)
    xv, yv, zv = np.meshgrid(x, x, x)

    B_field = np.vectorize(calculate_magnetic_field, signature='(),(),()->(n)')(xv, yv, zv)
    Bx = B_field[:, :, :, 0]
    By = B_field[:, :, :, 1]
    Bz = B_field[:, :, :, 2]

    # Bx[Bx > 20] = 20
    # By[By > 20] = 20
    # Bz[Bz > 20] = 20
    #
    # Bx[Bx < -20] = -20
    # By[By < -20] = -20
    # Bz[Bz < -20] = -20

    data = calculate_plot_data(xv, yv, zv, Bx, By, Bz)

    layout = calculate_plot_layout()

    fig = go.Figure(data=data, layout=layout)
    fig.add_scatter3d(x=lx, y=ly, z=lz, mode='lines',
                      line=dict(color='green', width=10))

    fig.write_html('3dplot.html')


def calculate_plot_data(xv, yv, zv, Bx, By, Bz):
    data = go.Cone(x=xv.ravel(), y=yv.ravel(), z=zv.ravel(),
                   u=Bx.ravel(), v=By.ravel(), w=Bz.ravel(),
                   colorscale='Inferno', colorbar=dict(title='$x^2$'),
                   sizemode="absolute", sizeref=20)

    return data


def calculate_plot_layout():
    layout = go.Layout(title=r'Plot Title',
                       scene=dict(xaxis_title=r'x',
                                  yaxis_title=r'y',
                                  zaxis_title=r'z',
                                  aspectratio=dict(x=1, y=1, z=1),
                                  camera_eye=dict(x=1.2, y=1.2, z=1.2)))

    return layout
