# # task1
# # import numpy as np
# # arr = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
# # result = arr + 10

# # print("Resulting Array:\n", result)


# # task2
# import numpy as np
# table = np.arange(1, 13).reshape(4, 3)
# row = np.array([5, 15, 25])
# result = table + row
# print("Table Shape :", table.shape)
# print("Row Shape   :", row.shape)
# print("Result Shape:", result.shape)
# print("Result Array:\n", result)


# task3
# import numpy as np
# arr1 = np.ones((3, 4), dtype=int)
# arr2 = np.array([10, 20, 30])

# try:
#     bad_sum = arr1 + arr2
# except ValueError as err:
#     print("Captured Error:", err)
# arr2_fixed = arr2.reshape(-1, 1)
# fixed_result = arr1 + arr2_fixed
# print("Fixed Resulting Array:\n", fixed_result)


# task4
# import numpy as np
# np.random.seed(42)
# arr = np.random.uniform(10.0, 50.0, size=(5, 2))
# col_means = arr.mean(axis=0)
# centred_arr = arr - col_means

# print("Original Array:\n", np.round(arr, 3))
# print("Column Means  :", np.round(col_means, 3))
# print("Centred Result:\n", np.round(centred_arr, 3))




# task5
import numpy as np
np.random.seed(101)
raw_features = np.random.normal(loc=50, scale=15, size=(10, 3))

standardised_features = (raw_features - raw_features.mean(axis=0)) / raw_features.std(axis=0)
print("Standardised Feature Array:\n", np.round(standardised_features, 4))