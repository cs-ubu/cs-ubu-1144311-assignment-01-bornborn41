import numpy.linalg as linalg
import numpy as np

A = np.array([
    [4.0, -2.0,  1.0],
    [-2.0,  4.0, -2.0],
    [1.0, -2.0,  3.0]])
b = np.array([1.0, 4.0, 2.0])
print(np.dot(A, b))
# linalg.inv(A)
# linalg.det(A)
# linalg.solve(A, b)
