import numpy as np

vectors = np.arange(3, 9).reshape(2, 3)
vector_sum = np.sum(vectors, axis=0)
print(vector_sum)