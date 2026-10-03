import numpy as np

readings = np.array([25.4, 28.1, -5.0, 30.2, -1.2, 27.8, 29.0, 31.5, -9.9, 26.3])

readings[readings < 0] = 0

matrix = readings.reshape(2, 5)

row_mean = np.mean(matrix, axis=1)

print("Cleaned Matrix:\n", matrix)
print("Row Mean:", row_mean)