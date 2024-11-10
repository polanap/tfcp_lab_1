import numpy as np
import matplotlib.pyplot as plt


def julia_set(c, x_range, y_range, resolution, max_iter):
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    Z = np.meshgrid(x, y)
    Z = Z[0] + 1j * Z[1]

    img = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 1000
        img[mask] = i
        Z[mask] = Z[mask] ** 2 + c

    return img


def plot_julia(c, x_range, y_range, resolution=800, max_iter=256):
    img = julia_set(c, x_range, y_range, resolution, max_iter)
    plt.imshow(img, extent=(x_range[0], x_range[1], y_range[0], y_range[1]), cmap='twilight_shifted')
    plt.colorbar()
    plt.title(f'Заполненное множество Жюлиа для c = {c}')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()


c = 1 + 1j
plot_julia(c, x_range=(-1.5, 1.5), y_range=(-1.5, 1.5), resolution=1000, max_iter=500)
