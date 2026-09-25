# import numpy as np

# # Create NumPy array
# arr = np.array([10, 20, 30, 40, 50])

# # Print array and its properties
# print("Array:", arr)
# print("Shape:", arr.shape)
# print("Data Type (dtype):", arr.dtype)



# import numpy as np

# data = np.array([1, 2, 3, 4, 5])

# # Single line vectorised multiplication (no loops)
# result = data * 10

# print("Resulting Array:")
# print(result)




# import numpy as np

# # Seed for reproducible random integers
# np.random.seed(42)
# arr = np.random.randint(1, 100, size=6)

# # Create boolean mask for values > 50
# mask = arr > 50

# # Apply mask to filter array
# filtered_arr = arr[mask]

# print("Original Array:", arr)
# print("Boolean Mask (> 50):", mask)
# print("Filtered Array:", filtered_arr)



# import numpy as np

# vals = np.array([15, 42, 8, 91, 23])

# # Set elements less than 20 to 0 in-place
# vals[vals < 20] = 0

# print("Final Modified Array:")
# print(vals)



# import numpy as np

# # 2D array representing test scores (3 students x 4 subjects)
# scores = np.array([
#     [80, 40, 90, 30],
#     [70, 60, 50, 80],
#     [20, 30, 40, 10]
# ])

# # Extract all scores 60 or above using boolean indexing
# high_scores = scores[scores >= 60]

# print("Extracted Scores (>= 60):")
# print(high_scores)