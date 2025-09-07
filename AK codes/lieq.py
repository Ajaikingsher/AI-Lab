import numpy as np

print("===== MATRIX OPERATIONS =====")

A = np.array([list(map(float, input("Enter row of Matrix A: ").split())) for _ in range(int(input("Rows in A: ")))])
B = np.array([list(map(float, input("Enter row of Matrix B: ").split())) for _ in range(int(input("Rows in B: ")))])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

if A.shape == B.shape:
    print("\nA + B =\n", A + B)
    print("A - B =\n", A - B)
else:
    print("\nAddition/Subtraction not possible")

print("\nTranspose of A:\n", A.T)
print("Transpose of B:\n", B.T)

if A.shape[1] == B.shape[0]:
    print("\nA x B =\n", A @ B)
else:
    print("\nMultiplication not possible")
