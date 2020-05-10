import numpy as np

x_data = np.load('x_data.npy')
y_data = np.load('y_data.npy')

print(x_data.shape, y_data.shape)
print(x_data[:10])
print(y_data[:10])
