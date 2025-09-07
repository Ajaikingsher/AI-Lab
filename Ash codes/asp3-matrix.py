import numpy as np
def mat(name):
    r, c = map(int, input(f"Enter rows and cols of {name}: ").split())
    print("Enter elements row by row:")
    data = []
    for i in range(r):
        row = list(map(float, input().split()))
        data.append(row)
    return np.array(data)

print("MATRIX OPERATIONS")
A = mat("Matrix A")
B = mat("Matrix B")

print("Matrix A + B =")
print(A + B)

print("Matrix A - B =")
print(A - B)

print("Transpose of A =")
print(A.T)

print("Transpose of B =")
print(B.T)

print("Matrix A x B =")
print(A @ B)