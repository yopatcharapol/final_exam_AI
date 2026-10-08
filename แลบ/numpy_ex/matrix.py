import numpy as np

# Create two matrices
matrix_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_b = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Matrix multiplication
result_multiplication = np.matmul(matrix_a, matrix_b)

# Matrix dot product
result_dot_product = np.dot(matrix_a, matrix_b)

# Display the results
print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nMatrix Multiplication:")
print(result_multiplication)

print("\nMatrix Dot Product:")
print(result_dot_product)

# 2 rows, 2 columns, in 3 layers 
a = np.random.rand(3,2,2)  
b = np.random.rand(3,2,2) 

# perform matrix multiplication
c = np.dot(a, b)
d = np.matmul(a,b) # a @ b

print(c.shape)
print(d.shape)
