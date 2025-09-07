import numpy as np

n = int(input("Enter number of variables: "))

A, B = [], []
for i in range(n):
    A.append(list(map(float, input("Enter coefficients of Eq{i+1}: ").split())))
    B.append(float(input("Enter constant of Eq{i+1}: ")))

X = np.linalg.solve(np.array(A), np.array(B))

print("Solution:")
for i, val in enumerate(X, 1):
    print("x", i, "=", val)
