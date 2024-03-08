import numpy as np
import matplotlib.pyplot as plt

# Создание массива нулей
shape = (100, 100)
gradient = np.zeros(shape)

# Заполнение массива градиентом
for i in range(shape[0]):
    for j in range(shape[1]):
        gradient[i, j] = i + j

# Построение изображения
plt.imshow(gradient)
plt.show()