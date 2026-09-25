# import numpy as np

# # Create the original array
# arr = np.array([10, 20, 30, 40, 50])

# # Fancy indexing to pick indices 4, 0, and 4
# result = arr[[4, 0, 4]]

# print("Original Array:", arr)
# print("Indexed Array:", result)



# import numpy as np

# data = np.array([15, 25, 35, 45, 55])

# # Single line mask using bitwise OR (|) with required parentheses
# filtered_data = data[(data > 40) | (data < 20)]

# print("Filtered Array:", filtered_data)




# import numpy as np

# # Create 1-D array with 12 elements
# arr12 = np.arange(12)

# # Reshape into 3 rows, inferring columns with -1
# reshaped_arr = arr12.reshape(3, -1)

# print("Reshaped Array:\n", reshaped_arr)
# print("Resulting Shape:", reshaped_arr.shape)

# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Vertical and Horizontal Stacking
# v_result = np.vstack([a, b])
# h_result = np.hstack([a, b])

# print("Vertical Stack (vstack):\n", v_result)
# print("Horizontal Stack (hstack):\n", h_result)







# import numpy as np

# # 1. Create 1-D array and reshape to 2-D column vector
# vec1 = np.array([10, 20, 30, 40, 50, 60]).reshape(-1, 1)

# # 2. Create second 2-D column vector
# vec2 = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# # 3. Concatenate along axis 1 to produce a (6, 2) matrix
# final_matrix = np.concatenate([vec1, vec2], axis=1)

# print("Concatenated (6, 2) Array:\n", final_matrix)
# print("Final Shape:", final_matrix.shape)



