import numpy as np
import matplotlib.pyplot as plt

# Размер изображения
width, height = 100, 100

# Коэффициенты авторегрессии
phi_1_values = [-0.5, 0, 0.5]
phi_2_values = [-0.5, 0, 0.5]

# Генерация белого шума
epsilon = np.random.normal(loc=0, scale=1, size=(width, height))

# Инициализация изображения
I = np.zeros((width, height))

# Генерация изображений для различных значений phi_1 и phi_2
for phi_1 in phi_1_values:
    for phi_2 in phi_2_values:
        # Генерация изображения
        # # Для демонстрации
        # phi_1 = float(input('Введите значение phi_1: '))
        # phi_2 = float(input('Введите значение phi_2: '))
        for x in range(1, width):
            for y in range(1, height):
                I[x, y] = phi_1 * I[x-1, y] + phi_2 * I[x, y-1] + epsilon[x, y]
        
        # Построение изображения
        plt.figure(figsize=(5, 5))
        plt.imshow(I, cmap='gray')
        plt.title(f'phi_1 = {phi_1}, phi_2 = {phi_2}')
        plt.axis('off')
        plt.show()