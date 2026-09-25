# import numpy as np

# # Create the original 1-D array
# arr = np.array([1, 2, 3, 4])

# # Apply element-wise exponential function
# result = np.exp(arr)

# print("Original Array:", arr)
# print("Exponential Result:", result)


# import numpy as np

# # Probability distribution array from a classifier
# probabilities = np.array([0.1, 0.7, 0.2])

# # Find the position/index of highest probability
# predicted_class = probabilities.argmax()

# print("Probabilities:", probabilities)
# print("Predicted Class Index:", predicted_class)





# import numpy as np

# # Define vectors
# a = np.array([1, 2])
# b = np.array([3, 4])

# # Element-wise multiplication (* operator) -> Vector
# elem_wise = a * b

# # Dot product (@ operator) -> Scalar
# dot_prod = a @ b

# print("Element-wise Multiplication (a * b):", elem_wise)
# print("Dot Product (a @ b):", dot_prod)



# import numpy as np
# X = np.array([
#     [2, 1],
#     [4, 3],
#     [6, 5]
# ])

# w = np.array([0.5, 2.0])

# predictions = X @ w

# print("Feature Matrix X shape:", X.shape)
# print("Weight Vector w shape:", w.shape)
# print("Predictions Array (X @ w):", predictions)






import numpy as np

# Define weights and values arrays
weights = np.array([0.2, 0.5, 0.3])
values = np.array([80, 90, 70])

# Method 1: Sum of element-wise multiplication
method1_result = (weights * values).sum()

# Method 2: Dot product operator (@)
method2_result = weights @ values

print("Method 1 - sum(weights * values):", method1_result)
print("Method 2 - weights @ values:", method2_result)
print("Outputs are identical:", np.isclose(method1_result, method2_result))