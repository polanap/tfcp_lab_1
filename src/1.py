import numpy as np
import matplotlib.pyplot as plt

# Параметры изображения
width, height = 800, 800  # Размеры изображения
max_iter = 100  # Максимальное количество итераций
x_min, x_max = -2.0, 1.0  # Границы по оси x
y_min, y_max = -1.5, 1.5  # Границы по оси y
# x_min, x_max = -2.0, 2.0  # Границы по оси x
# y_min, y_max = -2.0, 2.0  # Границы по оси y


# Создание сетки комплексной плоскости
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y  # Матрица комплексных чисел

# Создаем массив для хранения количества итераций
mandelbrot_set = np.zeros(C.shape, dtype=int)

# Итерационный процесс для каждого C
for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        c = C[i, j]
        z = 0
        for k in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                mandelbrot_set[i, j] = k  # Сохраняем количество итераций до "убегания"
                break
        else:
            mandelbrot_set[i, j] = max_iter  # Если точка принадлежит множеству

# Визуализация
plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max), cmap='hot')
plt.colorbar(label='Количество итераций до "убегания"')
plt.title("Множество Мандельброта")
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
